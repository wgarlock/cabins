const { spawn } = require('child_process')
const path = require('path')
const fs = require('fs')
const packageJson = require('./package.json')
function parcelBuild (path) {
    const staticSrc = path + '/static_src'
    const file = path.substring(path.lastIndexOf('/') + 1)
    if (fs.existsSync(staticSrc)) {
        const cmd = 'NODE_ENV=production parcel build'
        const outDir = path + '/static'
        fs.rmdirSync(outDir, { recursive: true })
        const args = [staticSrc + '/index.js', '--out-dir ' + outDir, '--out-file cabins-' + file + '.' + packageJson.version + '.js', '--public-url /static/']
        console.log(cmd)
        console.log(args)
        const results = spawn(cmd, args, { shell: true })
        results.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`)
        })
        results.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`)
        })
        results.on('close', (code) => {
            console.log(`child process exited with code ${code}`)
        })
    }
}

const getAllFiles = function (dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath)
    arrayOfFiles = arrayOfFiles || []
    files.forEach(function (file) {
        if (fs.statSync(dirPath + '/' + file).isDirectory()) {
            parcelBuild(dirPath + '/' + file)
            arrayOfFiles = getAllFiles(dirPath + '/' + file, arrayOfFiles)
        } else {
            arrayOfFiles.push(path.join(__dirname, dirPath, '/', file))
        }
    })
    return arrayOfFiles
}

getAllFiles(__dirname)
