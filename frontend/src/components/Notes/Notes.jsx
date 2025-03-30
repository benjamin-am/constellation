import "../Notes/Notes.scss"

function Notes({ notesText, setNotesText }) {
    const handleChange = (e) => {
        setNotesText(e.target.value);
    };

    return (
        <div className="notesWrapper">
        <textarea 
        className="notesText" 
        placeholder="this is my notes area"
        value={notesText}
        onChange={handleChange}>

</textarea>

        </div>

    )
}

export default Notes;