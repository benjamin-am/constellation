import "../Notes/Notes.scss"

function Notes({ title, setTitle, notesText, setNotesText }) {
    const handleChange = (e) => {
        setNotesText(e.target.value);
    };
    const handleTitleChange = (e) => {
        setTitle(e.target.value);
    };

    return (
        <div className="notesWrapper">
        <input
        type="text"
        value={title}
        className="notesTitle"
        placeholder="your title goes here"
        onChange={handleTitleChange}/>

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