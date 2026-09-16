export default function Signup(){
	return (
		<div className="bg-[#FFF8E7] h-screen w-screen pt-30 flex justify-center items-center">
			<div className="text-[#6B8E3D] bg-[#FFFFFF] border-[#E4DFC9] border-2 min-w-15 min-h-87 p-5 w-1/5 h-2/3 rounded-3xl">
				<p className="font-bold text-3xl mb-5">Sign Up</p>
				<label className=" w-full my-2">
					Username: <br/>
					<input name="username" type="name" className="border-[#a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="jhoedon"/>
				</label>
				<label className=" w-full my-2">
                                        Password: <br/>
                                        <input name="password" type="password" className="border-[#a7e6a7] border-1 bg-[#e7ffe7]  rounded-lg mb-2 mt-1 w-full h-7" placeholder="Use strong password"/>
                                </label>
				<label className=" w-full my-2">
                                        Conform Password: <br/>
                                        <input name="password" type="password" className="border-[#a7e6a7] border-1 bg-[#e7ffe7]  rounded-lg mb-2 mt-1 w-full h-7" placeholder="Above Password"/>
                                </label>
				
				<button className="bg-[#d9822b] text-[#FFFFFF] rounded-xl w-full h-10 my-5">Join us</button>
			</div>
		</div>
	)
}
