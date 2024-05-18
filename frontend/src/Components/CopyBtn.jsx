import { memo, useState } from "react";
import { IoMdCopy } from "react-icons/io";

const CopyBtn = memo((props)=> {
    const [iconColor, setIconcolor] = useState("#3B82F6") ;
    const [isClicked, setIsClicked] = useState(false) ;
    return <div className="flex justify-center cursor-pointer">
    <IoMdCopy size={35} color={iconColor} onMouseOver={()=>{
        setIconcolor("#1b5ef2");}
    } onMouseOut={()=> {
        setIconcolor("#3B82F6")
    }}
    onClick={
        ()=> {
            copyToClipboard(props.data) && setIsClicked(true) ;
            setTimeout(() => {
                setIsClicked(false);
              }, 1000);
        }}/>
    {isClicked && <span className=" text-xs">Copied!</span>}
    </div>
})

async function copyToClipboard(variable) {
    try {
      await navigator.clipboard.writeText(variable);
      return true ;
    } catch (err) {
      return false
    }
} 

export default CopyBtn ;