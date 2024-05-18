import { memo } from 'react';
import '../index.css'

const InputBox = memo( (props)=> {
    return <div className="inputBox" >
        <input type="text" name={props.name} placeholder={props.placeHolder} readOnly={props.readOnly}
        className={props.className} value={props.value} onClick={props.onClick} onChange={props.onChange} onKeyDown={props.onKeyDown}/>
    </div>
})

export default InputBox ;