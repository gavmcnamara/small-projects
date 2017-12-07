function madLibs() {

    var mystory = document.getElementById("mystory");
    var thing = document.getElementById("thing").value;
    var title = document.getElementById("title").value;
    var adjective = document.getElementById("adjective").value;
    var verb = document.getElementById("verb").value;
    var noun = document.getElementById("noun").value;

    mystory.innerHTML = "There once was this huge " + thing + ".  Inside of this "
    + thing + " lived a " + title + ". It was frendly but " + adjective +
    ". It loved " + noun + " and wants you to as well!";

}