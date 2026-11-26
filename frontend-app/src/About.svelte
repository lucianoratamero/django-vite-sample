<svelte:head>
	<title>About</title>
</svelte:head>

<article
	class="mx-auto prose prose-lg prose-headings:text-sea-green-900 prose-a:text-spray-600 hover:prose-a:text-gold-drop-700 prose-code:text-gold-drop-700 prose-code:before:content-none prose-code:after:content-none"
>
	<h1>About</h1>
	<p>
		A sample Svelte app meant to be served by Django through
		<a href="https://github.com/MrBin99/django-vite">django-vite</a>.
	</p>

	<h2>Stack</h2>
	<ul>
		<li>Django 6 + django-vite on the backend</li>
		<li>Svelte 5 with runes, built with Vite</li>
		<li>Tailwind CSS 4 with the typography plugin</li>
	</ul>

	<h2>Palette</h2>
	<p>
		The colors come from <a href="https://lincolnloop.com">lincolnloop.com</a>: spray, sea green,
		gold drop, flare and nero. They're Tailwind theme colors in <code>src/app.css</code>, so classes
		like <code>bg-spray</code> and <code>text-sea-green-900</code> work out of the box.
	</p>
</article>
