const { exec } = require('child_process')
const path = require('path')
const fs = require('fs')

function parcelWatch (path) {
  const staticSrc = path + '/static_src'
  const file = path.substring(path.lastIndexOf('/') + 1)
  if (fs.existsSync(staticSrc)) {
    const cmd = 'NODE_ENV=development parcel watch'
    const args = [staticSrc + '/index.js', '--out-dir ' + path + '/static', '--out-file daash-' + file + '.js', '--public-url /static/']
    console.log(cmd, args)
    exec(cmd, args, (error, stdout, stderr) => {
      if (error) {
        console.log(`error: ${error.message}`)
        return
      }
      if (stderr) {
        console.log(`stderr: ${stderr}`)
        return
      }
      console.log(`stdout: ${stdout}`)
    })
  }
}

const getAllFiles = function (dirPath, arrayOfFiles) {
  const files = fs.readdirSync(dirPath)
  arrayOfFiles = arrayOfFiles || []
  files.forEach(function (file) {
    if (fs.statSync(dirPath + '/' + file).isDirectory()) {
      parcelWatch(dirPath + '/' + file)
      arrayOfFiles = getAllFiles(dirPath + '/' + file, arrayOfFiles)
    } else {
      arrayOfFiles.push(path.join(__dirname, dirPath, '/', file))
    }
  })
  return arrayOfFiles
}

getAllFiles(__dirname)