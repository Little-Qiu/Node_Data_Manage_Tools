/*
 * @Author: 作者：
 * @Date: 2022-06-08 17:02:26
 * @LastEditTime: 2022-06-08 17:02:51
 * @LastEditors: qlw
 * @Description: 描述
 * @FilePath: \Node_Data_Manage_Tools\index.js
 */
const { app, BrowserWindow } = require('electron')

function createWindow () {   
  // 创建浏览器窗口
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })
  // 加载index.html文件
  win.loadFile('./src/view/index.html')
}
app.on('ready', createWindow)
