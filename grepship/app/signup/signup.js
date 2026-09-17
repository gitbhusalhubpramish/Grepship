"use client"

import {useState, useEffect} from "react"

export default function Signup(){
	const [form, setform] = useState({username: "", password:"", conformpass: "", email:""})
	
	const handelChange=(e)=>{
		const {name,value}=e.target
		setform((prev)=>({...prev,[name]:value,}))
	}
	const handelSubmit = async ()=>{
		if (form.password !== form.conformpass){
			alert("password didn't matched")
		}
		const res = await fetch("api/register", {method: "POST", headers:{"Content-Type":"application/json"}, body: JSON.stringfy({form})})
		
		if (res.status===201){
			alert("signup successful")
		}
		if (res.status===500){
			alert("server error")
			
		}
		else if (res.status===400){
			alert(res.message)
		}
		
		
	}
	return (
		<div className="bg-[#FFF8E7] h-screen w-screen pt-30 flex justify-center items-center">
			
			<div className="text-[#6B8E3D] bg-[#FFFFFF] border-[#E4DFC9] border-2 min-w-15 min-h-102 p-5 w-1/5 h-2/3 rounded-3xl">
				<p className="font-bold text-3xl mb-5">Sign Up</p>
				<label className=" w-full my-2">
					Username: <br/>
					<input name="username" type="name" className="border-[#a7e6a7] border-1 bg-[#e7ffe7] rounded-lg mt-1 mb-2 w-full h-7" placeholder="jhoedon" value={form.username} onChange={(e)=> handelChange(e)}/>
				</label>
				<label className=" w-full my-2">
                                        Password: <br/>
                                        <input name="password" type="password" className="border-[#a7e6a7] border-1 bg-[#e7ffe7]  rounded-lg mb-2 mt-1 w-full h-7" placeholder="Use strong password" value={form.password} onChange={(e)=>handelChange(e)}/>
                                </label>
				<label className=" w-full my-2">
                                        Confirm Password: <br/>
                                        <input name="conformpass" type="password" className="border-[#a7e6a7] border-1 bg-[#e7ffe7]  rounded-lg mb-2 mt-1 w-full h-7" placeholder="Above Password" value={form.conformpass} onChange={(e)=>handelChange(e)}/>
                                </label>
				<label className=" w-full my-2">
                                        Email: <span className="text-sm text-top text-red-500">*optional</span> <br/>
                                        <input name="email" type="email" className="border-[#a7e6a7] border-1 bg-[#e7ffe7]  rounded-lg mt-1 w-full h-7" placeholder="jhoedon@example.com" value={form.email} onChange={(e)=>handelChange(e)}/>
                                </label>
		
				<button className="bg-[#d9822b] cursor-pointer text-[#FFFFFF] rounded-xl w-full h-10 my-5">Join us</button>
		
			</div>
		</div>
	)
}
