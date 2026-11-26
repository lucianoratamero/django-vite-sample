<script lang="ts">
	import { onMount } from 'svelte';

	type Todo = { id: number; text: string; done: boolean };

	// The Django REST framework TodoViewSet. VITE_API_HOST is Django's origin (see .env.example).
	const API = `${import.meta.env.VITE_API_HOST ?? ''}/api/todos/`;

	let todos = $state<Todo[]>([]);
	let loaded = $state(false); // hides the count and list until the first load, instead of "0 of 0"
	let text = $state('');
	let error = $state('');

	const remaining = $derived(todos.filter((t) => !t.done).length);

	// Sends a change to the API. On failure it shows the error, then rethrows so the caller can skip or undo its change.
	async function api<T>(path: string, method: string, body?: object): Promise<T> {
		error = '';
		try {
			const res = await fetch(API + path, {
				method,
				headers: { 'Content-Type': 'application/json' },
				body: body && JSON.stringify(body)
			});
			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			return (res.status === 204 ? undefined : await res.json()) as T; // DELETE returns no body
		} catch (e) {
			error = `Couldn't reach the API (${method} ${API}${path}): ${(e as Error).message}`;
			throw e;
		}
	}

	onMount(async () => {
		try {
			todos = await api<Todo[]>('', 'GET');
			loaded = true;
		} catch {
			// api() already showed the error
		}
	});

	async function add(event: SubmitEvent) {
		event.preventDefault();
		const value = text.trim();
		if (!value) return;
		try {
			todos.push(await api<Todo>('', 'POST', { text: value }));
			text = '';
		} catch {
			// api() already showed the error; keep the text so it can be retried
		}
	}

	async function toggle(todo: Todo) {
		try {
			await api(`${todo.id}/`, 'PATCH', { done: todo.done });
		} catch {
			todo.done = !todo.done; // checkbox already flipped locally, put it back
		}
	}

	async function remove(id: number) {
		try {
			await api(`${id}/`, 'DELETE');
			todos = todos.filter((t) => t.id !== id);
		} catch {
			// api() already showed the error; keep the row
		}
	}
</script>

<svelte:head>
	<title>Todos · Svelte</title>
</svelte:head>

<section class="mx-auto max-w-xl">
	<h1 class="text-4xl font-bold text-sea-green-900">Todos</h1>
	{#if loaded}
		<p class="mt-2 text-sea-green-600">{remaining} of {todos.length} left to do</p>
	{/if}

	<form onsubmit={add} class="mt-8 flex gap-2">
		<label for="new-todo" class="sr-only">New todo</label>
		<input
			id="new-todo"
			bind:value={text}
			placeholder="What needs doing?"
			class="flex-1 rounded-lg border border-nero-200 bg-white px-4 py-2 focus:border-spray-500 focus:ring-2 focus:ring-spray focus:outline-none"
		/>
		<button
			class="rounded-lg bg-spray px-5 py-2 font-semibold text-sea-green-950 hover:bg-spray-400"
		>
			Add
		</button>
	</form>

	{#if error}
		<p role="alert" class="mt-4 rounded-lg bg-gold-drop-400/15 px-4 py-2 text-gold-drop-800">
			{error}
		</p>
	{/if}

	{#if loaded}
		<ul class="mt-6 divide-y divide-nero-100 rounded-lg border border-nero-200 bg-white shadow-sm">
			{#each todos as todo (todo.id)}
				<li class="flex items-center gap-3 px-4 py-3">
					<input
						id="todo-{todo.id}"
						type="checkbox"
						bind:checked={todo.done}
						onchange={() => toggle(todo)}
						class="size-5 accent-spray-500"
					/>
					<label
						for="todo-{todo.id}"
						class={['flex-1', todo.done && 'text-sea-green-600 line-through']}
					>
						{todo.text}
					</label>
					<button
						onclick={() => remove(todo.id)}
						aria-label="Delete “{todo.text}”"
						class="rounded-md px-2 py-1 text-sea-green-600 hover:bg-gold-drop-400/15 hover:text-gold-drop-700"
					>
						✕
					</button>
				</li>
			{:else}
				<li class="px-4 py-8 text-center text-sea-green-600">All done.</li>
			{/each}
		</ul>
	{/if}
</section>
