import { svelteDevtools } from '@sveltejs/vite-devtools-svelte';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [svelteDevtools(), tailwindcss(), svelte()],
	devtools: { apply: 'serve', clientAuth: true }
	// base: '/static',
	// build: {
	// 	manifest: 'manifest.json',
	// 	rolldownOptions: { input: ['index.html', 'src/main.ts'] }
	// }
});
