<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />
<div class="half-circle-container">
	<div class="half-circle" />
	<a href="#" class="play-link">
		<img src="/play.png" alt="Play" />
	</a>
</div>

<style>
	.half-circle-container {
		position: relative;
		margin-left: 15.46875vw;
		margin-top: -8rem;
		width: 91.875vw;
	}
	.half-circle {
		position: relative;
		width: 100%;
		aspect-ratio: 2/1;
		background-color: #efb0c9;
		border-top: 0;
		border-bottom-left-radius: 91.875vw;
		border-bottom-right-radius: 91.875vw;
		z-index: -1;
		padding-bottom: 0rem;
		margin-bottom: 4.5rem;
	}

	.play-link {
		position: absolute;
		display: block;
		bottom: -4.5rem;
		z-index: 5;
		background-color: #eee;
		border-radius: 5rem;
		margin: auto auto 0 auto;
		left: 0;
		right: 0;
		width: 10rem;
		height: 10rem;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.play-link img {
		width: 9rem;
		height: 9rem;
	}
</style>
