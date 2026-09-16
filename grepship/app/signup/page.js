export default function Signup(){
	return (
		<div className="bg-[#FFF8E7] h-screen w-screen pt-30 flex justify-center items-center">
			<div className="text-[#6B8E3D] bg-[#FFFFFF] border-[#E4DFC9] border-2 min-w-15 min-h-70 w-1/5 h-2/3 rounded-3xl">
				<p className="font-bold text-3xl m-5">Sign Up</p>
				<label className="m-5">
					Username: <br/>
					<input name="username" type="name" className="border-[#a7e6a7] border-1 bg-[#e7ffe7] mx-5 rounded-lg" placeholder="jhoedon"/>
				</label>
			</div>
		</div>
	)
}
