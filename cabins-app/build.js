const { spawnSync } = require('child_process')
const path = require('path')
const fs = require('fs')

function parcelBuild (path) {
  const staticSrc = path + '/static_src'
  const file = path.substring(path.lastIndexOf('/') + 1)
  if (fs.existsSync(staticSrc)) {
    const cmd = 'NODE_ENV=production parcel build'
    const args = [staticSrc + '/index.js', '--out-dir ' + path + '/static', '--out-file lodges-' + file + '.js', '--public-url /static/']
    console.log(cmd)
    console.log(args)
    spawnSync(cmd, args)
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
