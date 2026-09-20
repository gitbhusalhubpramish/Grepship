"use client"

import {useState, useEffect} from "react"
import Link from "next/link"

export default function Login(){

	const [form, setform] = useState({username: "", password:""})

	const handelChange=(e)=>{
		const {name, value} = e.target
		setform((prev=>({...prev, [name]:value,})))
	}
	
	const handelSubmit = async (e)=>{
		e.preventDefault()
		const res = await fetch("api/auth/login", {method: "POST", headers:{"Content-Type":"application/json", "Accept": "application/json"}, body: JSON.stringify({username:form.username, password:form.password})})
		if (res.status===200){
			alert("Login successful")
		}
		else if (res.status===500){
			alert("server error")
		}
		else if (res.status===400){
			alert(res.message)
		}
		else {
			alert("something went wrong")
		}
	}
	return (
		<div className="bg-[#FFF8E7] h-screen w-screen pt-30 flex justify-center items-center">
			<form className="text-[#6B8E3D] bg-[#ffffff] border-[#e4dfc9] border-2 min-w-15 min-h-82 p-5 w-1/5 h-2/3 rounded-3xl" onSubmit={handelSubmit}>
				<p className="font-bond text-3xl mb-5">Login</p>
				<label className="w-full my-2">
					Username: <br/>
					<input name = "username" type="name" className="border-[#a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="jhoedon" value={form.username} onChange={(e)=>handelChange(e)} required/>
				</label>
				<label className="w-full my-2">
					Password: <br/>
					<input name="password" type="password" className="border-[a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="P@s$word" value={form.password} onChange={(e)=>handelChange(e)} required/>
				</label>
				<button type="submit" className="bg-[#d9822b] cursor-pointer text-[#ffffff] rounded-xl w-full h-10 my-5">Login</button>
				<p className="text-sm ">Not having an account? <Link className="ml-1 inline text-blue-500 underline" href="/signup">Signup</Link></p>
			</form>
		</div>
	)
}
