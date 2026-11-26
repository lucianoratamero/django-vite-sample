<script lang="ts">
	import { createRouter, Router } from 'sv-router';
	import About from './About.svelte';
	import NotFound from './NotFound.svelte';
	import Todos from './Todos.svelte';

	const { isActive } = createRouter({ '/': Todos, '/about': About, '*': NotFound });

	const links = [
		{ href: '/', label: 'Todos' },
		{ href: '/about', label: 'About' }
	] as const;
</script>

<div class="flex min-h-screen flex-col bg-nero-50 text-nero-900">
	<header class="bg-sea-green-900 text-white">
		<nav class="mx-auto flex max-w-3xl items-center justify-between px-6 py-4">
			<a href="/" class="text-lg font-bold tracking-tight">
				<span class="text-spray">django</span>-vite-sample
			</a>
			<ul class="flex gap-1">
				{#each links as link (link.href)}
					<li>
						<a
							href={link.href}
							aria-current={isActive(link.href) ? 'page' : undefined}
							class="rounded-md px-3 py-2 text-spray-100 hover:bg-sea-green-800 hover:text-white aria-[current=page]:bg-sea-green-800 aria-[current=page]:text-spray"
						>
							{link.label}
						</a>
					</li>
				{/each}
			</ul>
		</nav>
	</header>

	<main class="mx-auto w-full max-w-3xl flex-1 px-6 py-12">
		<Router />
	</main>

	<footer class="bg-sea-green-950 py-6 text-center text-sm text-spray-200">
		Colors borrowed from <a
			href="https://lincolnloop.com"
			class="underline hover:text-gold-drop-400"
		>
			lincolnloop.com
		</a>
	</footer>
</div>
