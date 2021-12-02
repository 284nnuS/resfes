<script context="module">
	/** @type {import('@sveltejs/kit').ErrorLoad} */
	export function load({ error, status }) {
		return {
			props: {
				code: status
			}
		};
	}
</script>

<script>
	import { goto } from '$app/navigation';

	export let code;

	let messages = {
		404: 'The page is not found, please check URL in address bar and try again'
	};
</script>

<main>
	<p
		style="
			color: rgba(29, 78, 216, 1);
			font-size: 6rem;
			font-weight:700;
			margin: 0
		"
	>
		{code}
	</p>
	<p
		style="
		font-weight: 700;
		font-size: 1.5rem;
	"
	>
		{messages[code]}
	</p>
	<button on:click={() => goto('/')}>Take Me Back</button>
</main>

<style>
	main {
		width: 100vw;
		height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}

	button {
		width: 13rem;
		height: 3.5rem;
		color: rgba(29, 78, 216, 1);
		border-radius: 3.25rem;
		background-color: #fff;
		border: 3px solid rgba(29, 78, 216, 1);
		margin: 1rem 0;
		font-size: 1.25rem;
		font-weight: 700;
	}

	button:hover {
		color: #fff;
		background-color: rgba(29, 78, 216, 1);
	}
</style>
