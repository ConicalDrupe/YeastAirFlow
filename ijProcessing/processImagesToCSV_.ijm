/*
 * Macro template to process multiple images in a folder
 */

#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output directory", style = "directory") output
#@ String (label = "File suffix", value = ".JPG") suffix
//


// function to scan folders/subfolders/files to find files with correct suffix
function processFolder(input) {
    list = getFileList(input);
    for (i = 0; i < list.length; i++) {
        if (File.isDirectory(input + File.separator + list[i])) {
            processFolder("" + input + File.separator + list[i]);
        }
        if (endsWith(list[i], suffix)) {
            processFile(input, output, list[i]);
        }
    }
}

function processFile(input, output, file) {
    open(input + File.separator + file);
    // Processing commands start here
    run("8-bit");
    run("Auto Threshold", "method=Yen white");
    run("Set Scale...", "distance=0 known=0 unit=pixel");
    run("Set Measurements...", "area mean shape feret's limit display redirect=None decimal=3");
    run("Analyze Particles...", "size=100-10000 display exclude clear add");
    // Processing commands end here
    // Now I wish to save the output to a csv file
    name = output + "/" + File.nameWithoutExtension + ".csv";
    saveAs("Results", name);
    close();
}
setBatchMode(true);
processFolder(input);

