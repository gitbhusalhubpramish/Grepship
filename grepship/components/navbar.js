export default function Navbar(){
	return (
		<nav className="flex fixed top-0 left-0 right-0 h-30 ">
			<div className="items-center">
				<a className="hover-scale-105">
					<img
						src="/logo.png"
						alt="grepship"
					/>
				</a>
			</div>
			<div>
				<input className="" type="text"/>
			</div>
		</nav>
	)
}
