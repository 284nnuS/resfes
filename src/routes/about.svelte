<script>
	import Navbar from '../components/navbar.svelte';
	import Footer from '../components/footer.svelte';

	function preload(src) {
		return new Promise(function (resolve) {
			let img = new Image();
			img.onload = resolve;
			img.src = src;
		});
	}
</script>

<Navbar />
<main>
	<div id="image-grid">
		<div class="card">
			<div class="images">
				<img src="./TDung.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Trung Dũng</p>
			</div>
		</div>
		<div class="card">
			<div class="images">
				<img src="./TDungg.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Thuỳ Dung</p>
			</div>
		</div>
		<div class="card">
			<div class="images">
				<img src="./VChuong.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Văn Chương</p>
			</div>
		</div>
		<div class="card">
			<div class="images">
				<img src="./Mentor.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Gia Trí</p>
			</div>
		</div>
		<div class="card">
			<div class="images">
				<img src="./THoai.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Thu Hoai</p>
			</div>
		</div>
		<div class="card">
			<div class="images">
				<img src="./VSon.jpg" alt="" />
			</div>
			<div class="description">
				<p class="name">Văn Sơn</p>
			</div>
		</div>
	</div>
</main>
<Footer />

<style>
	main {
		background-color: #efb0c9;
		width: 100vw;
		padding-top: 8rem;
		margin-bottom: 6rem;
		height: calc(100vh - 6rem - 8rem);
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}

	#image-grid {
		display: inline-grid;
		grid-template-columns: repeat(6, 10%);
		column-gap: calc(1rem + 2%);
		justify-content: center;
		height: 80%;
		width: 100%;
	}
	.card {
		border-radius: 20px;
		overflow: hidden;
		position: relative;
		box-shadow: 0 1px 10px 0px;
		justify-self: center;
		width: 100%;
		height: 100%;
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
		display: flex;
		flex-direction: column;
		justify-content: center;
	}
	.description p {
		font-size: 1.25rem;
		text-align: center;
		font-weight: 700;
		color: #fff;
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
	#image-grid .card:nth-child(1) img {
		transform: scale(1.1) translate(3%, 4%);
	}
	#image-grid .card:nth-child(2) img {
		transform: scale(1.2) translate(5%, -8%);
	}
	#image-grid .card:nth-child(3) img {
		transform: scale(1.1);
	}
	#image-grid .card:nth-child(4) img {
		transform: scale(1.2) translate(0, -4%);
	}
	#image-grid .card:nth-child(5) img {
		transform: scale(1.5) translate(-5%, -2%);
	}
	#image-grid .card:nth-child(6) img {
		transform: scale(1.5) translate(3%, -1%);
	}

	#image-grid .card:hover {
		transform: scale(1.03);
		transition: 0.5s ease-in-out;
	}
</style>
