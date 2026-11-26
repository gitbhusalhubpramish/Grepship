"use client"
import {useSearchParams} from "next/navigation"
import {useState, useEffect} from "react"

export default function Search(){
	const searchParams= useSearchParams()

	const [users, setusers] = useState(null)

	const query = searchParams.get("q") || ""
	useEffect( async ()=>{
		if (!query) return
		const res = await fetch(`/api/search/search?q=${query}`)
		const data = res.json()
		if (data.users){
			setusers(data.users)
		}
		
	}, query)
	return (
		<div className="p-100 bg-[#fff8e7]">

		</div>
	)
}
