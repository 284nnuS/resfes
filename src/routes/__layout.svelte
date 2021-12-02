<script context="module">
	export const load = async ({ page }) => ({
		props: {
			key: page.path
		}
	});
</script>

<script>
	import 'normalize.css';
	import 'font-awesome/css/font-awesome.css';
	import Transition from '../components/transition.svelte';

	export let key;
</script>

<div class="flex-layout">
	<Transition refresh={key}>
		<slot />
	</Transition>
</div>

<style>
	.flex-layout {
		font-family: Poppins;
	}
</style>
