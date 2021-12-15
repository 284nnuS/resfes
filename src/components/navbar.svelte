<script>
	export let color = '#ffffff';

	$: cssVarStyles = `--name-color:${color}`;
</script>

<div class="navbar" style={cssVarStyles}>
	<div class="navbar-left">
		<ul>
			<li class="team-name">
				<a href="/">ZOOMI<br />DSOON</a>
			</li>
			<li>
				<a href="about">Giới thiệu</a>
			</li>
			<li>
				<a href="reason">Đôi lời</a>
			</li>
		</ul>
	</div>
	<div class="navbar-right">
		<img src="/fptedu.png" class="nav-logo" alt="FPT Education Logo" />
		<img src="/resfes.png" class="nav-logo" alt="Resfes Logo" />
	</div>
</div>

<style>
	.navbar {
		position: fixed;
		height: 6rem;
		padding: 3rem 3rem 0 3rem;
		top: 0;
		left: 0;
		right: 0;
		z-index: 10;
		display: flex;
		justify-content: space-between;
	}

	.navbar-left,
	.navbar-right {
		display: flex;
		align-items: center;
	}

	.navbar-left ul {
		list-style-type: none;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-left: 2.5vw;
		gap: calc(10vw - 1rem);
	}

	.navbar-left li {
		padding: 0;
	}

	.navbar-left ul li a {
		text-decoration: none;
		color: #fff;
		font-size: 1.5rem;
		display: block;
		padding: 0;
		display: block;
		font-weight: 800;
		width: 8rem;
		line-height: 5rem;
		height: 5rem;
		text-align: center;
	}

	.navbar-left ul li.team-name a {
		color: var(--name-color, white) !important;
		font-weight: 700;
		font-size: 2rem;
		line-height: 2.5rem;
		margin: 0;
	}

	.nav-logo {
		height: 4rem;
		margin-left: 3rem;
	}
</style>
