<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />
<main>
	<center class="container">
		<div id="wrap-images">
			<div class="card">
				<div class="images">
					<img src="./TDung.jpg" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Trung Dũng</p>
					<p class="id">DE150256</p>
				</div>
			</div>
			<div class="card">
				<div class="images">
					<img src="./TDungg.jpeg" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Thuỳ Dung</p>
					<p class="id">DE150256</p>
				</div>
			</div>
			<div class="card">
				<div class="images">
					<img src="./VChuong.jpg" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Văn Chương</p>
					<p class="id">DE150256</p>
				</div>
			</div>
			<div class="card">
				<div class="images">
					<img src="./Mentor.jpg" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Gia Trí</p>
					<p class="id">DE150256</p>
				</div>
			</div>
			<div class="card">
				<div class="images">
					<img src="./THoai.png" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Thu Hoai</p>
					<p class="id">DE150334</p>
				</div>
			</div>
			<div class="card">
				<div class="images">
					<img src="./VSon.jpg" alt="Team Member" srcset="" />
				</div>
				<div class="description">
					<p class="name">Văn Sơn</p>
					<p class="id">DE150256</p>
				</div>
			</div>
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
	#wrap-images {
		width: 100%;
		display: flex;
		justify-content: center;
	}
	.card {
		margin: 0px 25px;
		border-radius: 20px;
		width: 200px;
		height: 480px;
		overflow: hidden;
		position: relative;
		margin-top: 3rem;
		box-shadow: 0 1px 10px 0px;
	}
	.card .images {
		width: 100%;
		height: calc(100% - 110px);
	}
	.card .description {
		background-color: #20519b;
		width: 100%;
		padding: 12px 0px;
		height: 90px;
	}
	.description p {
		font-size: 20px;
		text-align: center;
		line-height: 10px;
		font-family: Arial, Helvetica, sans-serif;
		color: #fff;
	}
	.container {
		height: 80%;
		padding-top: 3rem;
		
	}
	.images {
		width: 100%;
		height: calc(100% - 110px);
		overflow: hidden;
	}
	.images img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}
	#wrap-images .card:nth-child(1) img {
		transform: scale(1.1) translate(10px, 10px);
	}
	#wrap-images .card:nth-child(5) img {
		transform: scale(1.6) translate(-10px, -15px);
	}
	#wrap-images .card:nth-child(3) img {
		transform: scale(1.1) translateY(-10px);
	}
	#wrap-images .card:nth-child(4) img {
		transform: translateY(10px);
		transform: scale(3.3) translate(12px, -15px);
	}
	#wrap-images .card:nth-child(2) img {
		transform: scale(1.3) translateY(-40px) translate(8px, 10px);
	}
	#wrap-images .card:nth-child(6) img {
		transform: scale(1.7) translate(-5px, -20px);
	}
</style>
