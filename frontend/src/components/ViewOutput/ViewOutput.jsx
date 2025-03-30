import { useState, useEffect, useRef } from "react";
import axios from "axios";

import "../ViewOutput/ViewOutput.scss"

function ViewOutput( { notesText }) {
    const [response, setResponse] = useState(null);
    const prevWordCountRef = useRef(0);

    const currentText = (text) => {
        return text.trim().split(/\s+/).filter(Boolean).length;
    };

    //API call
    useEffect(() => {
        const currentWordCount = currentText(notesText);
        const prevWordCount = prevWordCountRef.current;

        if (currentWordCount >= 10 && prevWordCount < 10) {
        axios
          .get(
            `https://d020f81f-06af-4479-bcbc-0be7c8845f8d.mock.pstmn.io`
          )
          .then((res) => {
            setResponse(res.data);
            console.log("API Response", res.data);
          })
          .catch((error) => console.log(error));
      }

      prevWordCountRef.current = currentWordCount;

    }, [notesText]);


    return (
        <div className="viewOutputWrapper">
        
        <div className="viewOutput">
            
        {response ? 
            <span className="apiResponse">
            {JSON.stringify(response, null, 1)}
            </span> :
        
        <p>Start typing and will load shortly...</p>
    }
    
        </div>
        </div>

    )

}
export default ViewOutput;