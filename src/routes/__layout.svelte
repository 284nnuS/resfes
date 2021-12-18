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


<svelte:head>
    <link rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Nunito:300,400,500,700,800,900">
</svelte:head>

<style>
	.flex-layout {
		font-family: 'Nunito';
	}
</style>