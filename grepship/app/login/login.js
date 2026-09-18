"use client"

import {useState, useEffect} from "react"
import Link form "next/link"

export default function Login(){
	return (
		<div className="bg-[#FFF8E7] h-screen w-screen pt-30 flex justify-center items-center">
			<form className="text-[#6B8E3D] bg-[#ffffff] border-[#e4dfc9] border-2 min-w-15 min-h-87 p-5 w-1/5 h-2/3 rounded-3xl">
				<p className="font-bond text-3xl mb-5">Login</p>
				<label className="w-full my-2">
					Username: <br/>
					<input name = "username" type="name" className="border-[#a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="jhoedon" required/>
				</label>
				<label className="w-full my-2">
					Password: <br/>
					<input name="password" type="password" className="border-[a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="P@s$word" required/>
				</label>
				<p>Not having an account? <Link href="/signup">Signup</Link></p>
			</form>
		</div>
	)
}
