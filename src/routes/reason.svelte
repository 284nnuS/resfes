<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />

<main>
	<center>
		<div class="container" >
        <center>Đôi lời</center>
        </div>
        <div class="container-button">
		<a href="/" class="start-btn">
			<button type="submit">Home</button>
		</a>
        </div>
	</center>
</main>

<style>
	main {
		background-color: #efb0c9;
		width: 100vw;
		padding-top: 8rem;
		padding-bottom: 5rem;
		height: calc(100vh - 5rem - 8rem);
		display: flex;
		align-items: center;
		flex-direction: column;
	}
	center {
		width: 100%;
		height: 100%;
	}
	.container {
		height: 77%;
		width: 80%;
		background-color: white;
        border-radius:2rem;
        border: 6px solid #20519B;
	}
    .container-button{
        padding:5px;
    }
	.start-btn {
		align-self: center;
		margin-top: 0.5rem;
	}

	.start-btn button {
		width: 13rem;
		height: 3.5rem;
		color: #fff;
		background-color: #d184a3;
		border: 0;
		font-size: 1.5rem;
		font-weight: 700;
		border-radius: 5rem;
	}

	.start-btn button:hover {
		background-color: rgb(223, 149, 180);
		color: #fff;
		transition: color 0.3s ease-in;
	}
</style>
