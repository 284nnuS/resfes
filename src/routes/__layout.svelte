<script>
	import 'normalize.css';
	import 'font-awesome/css/font-awesome.css';

	import Footer from '../components/footer.svelte';
</script>

<div class="flex-layout">
	<slot />
	<Footer />
</div>

<style>
	.flex-layout {
		overflow: hidden;
		font-family: Poppins;
	}
</style>
