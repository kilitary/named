/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => ImageHelper
});
module.exports = __toCommonJS(main_exports);
var import_obsidian3 = require("obsidian");

// src/helpers.ts
var import_obsidian = require("obsidian");
var DEBUG_MODE = false;
var LOAD_IMAGE_BLOB_TIMEOUT = 5e3;
var NOTICE_TIMEOUT_INF = 5e5;
var NOTICE_TIMEOUT = 1800;
function dbg(...args) {
  if (DEBUG_MODE) {
    console.log.apply(console, ["[ImageHelper]", ...args]);
  }
}
async function convertImage(file, src, mime, extension, quality) {
  if (file == null) {
    dbg("convertImage() : given file is null ");
    return;
  }
  const originExtension = getExtension(src);
  const notice = new import_obsidian.Notice("Converting image...", NOTICE_TIMEOUT_INF);
  try {
    const blob = await loadImageBlob(src);
    let arrayBuffer = await doConvertImage(
      blob,
      mime,
      quality
    );
    notice.hide();
    if (arrayBuffer.byteLength > 0) {
      await this.app.vault.modifyBinary(file, arrayBuffer);
      const sourcePath = file.path;
      const newFilePath = sourcePath.replace(
        "." + originExtension,
        "." + extension
      );
      try {
        dbg(
          "convertImage() calls renameFile(): ",
          sourcePath,
          " to ",
          newFilePath
        );
        this.app.fileManager.renameFile(file, newFilePath);
      } catch (err) {
        new import_obsidian.Notice(`Failed to rename ${newFilePath}: ${err}`);
        throw err;
      }
      new import_obsidian.Notice("Image format changed", NOTICE_TIMEOUT);
    }
  } catch (e) {
    if (notice) {
      notice.hide();
    }
    console.log("Error, could not change the image!", e);
    new import_obsidian.Notice(e, NOTICE_TIMEOUT);
    new import_obsidian.Notice("Error, could not change the image!", NOTICE_TIMEOUT);
  }
}
function getFileByName(imgURL) {
  const fileBaseName = getBasename(imgURL);
  if (fileBaseName == null || fileBaseName == "") {
    dbg("getFileByName() cannot get file basename");
    return null;
  }
  const resolvedLinks = app.metadataCache.resolvedLinks;
  for (const [mdFile, links] of Object.entries(resolvedLinks)) {
    for (const [filePath, nr] of Object.entries(links)) {
      if (filePath.includes(fileBaseName)) {
        try {
          const AttachFile = app.vault.getAbstractFileByPath(filePath);
          if (AttachFile instanceof import_obsidian.TFile) {
            dbg("getFileByName() - found : ", filePath);
            return AttachFile;
          }
        } catch (error) {
          new import_obsidian.Notice("cannot get the image file");
          console.error(error);
          return null;
        }
      }
    }
  }
  return null;
}
function getBasename(fullpath) {
  let fileBaseName = fullpath;
  if (fileBaseName.indexOf("/") >= 0) {
    fileBaseName = fileBaseName.substring(
      fileBaseName.lastIndexOf("/") + 1
    );
  }
  if (fileBaseName.indexOf("?") > 0) {
    fileBaseName = fileBaseName.substring(0, fileBaseName.indexOf("?"));
  }
  return fileBaseName;
}
function getExtension(fullpath) {
  let filename = getBasename(fullpath);
  if (filename.indexOf("?") > 0) {
    filename = filename.substring(0, filename.indexOf("?"));
  }
  if (filename.indexOf(".") > 0) {
    filename = filename.substring(filename.lastIndexOf(".") + 1).toLowerCase();
  }
  return filename;
}
function doConvertImage(file, mime, quality) {
  return new Promise((resolve, reject) => {
    let reader = new FileReader();
    reader.onloadend = function(e) {
      if (e.target == null || e.target.result == null) {
        return;
      }
      let image = new Image();
      image.onload = function() {
        let canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");
        let imageWidth = image.width;
        let imageHeight = image.height;
        let data = "";
        canvas.width = imageWidth;
        canvas.height = imageHeight;
        if (context !== null) {
          context.fillStyle = "#fff";
          context.fillRect(0, 0, imageWidth, imageHeight);
          context.save();
          context.translate(imageWidth / 2, imageHeight / 2);
          context.drawImage(
            image,
            0,
            0,
            imageWidth,
            imageHeight,
            -imageWidth / 2,
            -imageHeight / 2,
            imageWidth,
            imageHeight
          );
          context.restore();
        }
        data = canvas.toDataURL(mime, quality);
        if (!data || data == "data:,") {
          reject(new Error("Image size might be too big!!"));
        }
        let arrayBuffer = null;
        try {
          arrayBuffer = base64ToArrayBuffer(data);
          resolve(arrayBuffer);
        } catch (e2) {
          reject(e2);
        }
      };
      image.src = e.target.result.toString();
    };
    reader.readAsDataURL(file);
  });
}
function base64ToArrayBuffer(code) {
  const parts = code.split(";base64,");
  const raw = window.atob(parts[1]);
  const rawLength = raw.length;
  const uInt8Array = new Uint8Array(rawLength);
  for (let i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }
  return uInt8Array.buffer;
}
async function loadImageBlob(imgSrc) {
  const loadImageBlobCore = () => {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.crossOrigin = "anonymous";
      image.onload = () => {
        const canvas = document.createElement("canvas");
        canvas.width = image.width;
        canvas.height = image.height;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(image, 0, 0);
        canvas.toBlob((blob) => {
          resolve(blob);
        });
      };
      image.onerror = () => {
        reject();
      };
      image.src = imgSrc;
    });
  };
  return withTimeout(LOAD_IMAGE_BLOB_TIMEOUT, loadImageBlobCore());
}
function withTimeout(ms, promise) {
  const timeout = new Promise((resolve, reject) => {
    const id = setTimeout(() => {
      clearTimeout(id);
      reject(`timed out after ${ms} ms`);
    }, ms);
  });
  return Promise.race([promise, timeout]);
}

// src/settings.ts
var import_obsidian2 = require("obsidian");
var ICSettingTab = class extends import_obsidian2.PluginSettingTab {
  constructor(app2, plugin) {
    super(app2, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian2.Setting(containerEl).setName("Quality").setDesc(`image quality (1.0 is the best quality).`).addDropdown(
      (toggle) => toggle.addOptions({
        "0.1": "0.1",
        "0.15": "0.15",
        "0.2": "0.2",
        "0.25": "0.25",
        "0.3": "0.3",
        "0.35": "0.35",
        "0.4": "0.4",
        "0.45": "0.45",
        "0.5": "0.5",
        "0.55": "0.55",
        "0.6": "0.6",
        "0.65": "0.65",
        "0.7": "0.7",
        "0.75": "0.75",
        "0.8": "0.8",
        "0.85": "0.85",
        "0.9": "0.9",
        "0.95": "0.95",
        "1.0": "1.0"
      }).setValue(this.plugin.settings.quality).onChange(async (value) => {
        this.plugin.settings.quality = value;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian2.Setting(containerEl).setName("X offset").setDesc("x offset value as number from mouse click point").addText(
      (text) => text.setValue(this.plugin.settings.offset_x).onChange(async (value) => {
        this.plugin.settings.offset_x = value;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian2.Setting(containerEl).setName("Y offset").setDesc("y offset value as number from mouse click point").addText(
      (text) => text.setValue(this.plugin.settings.offset_y).onChange(async (value) => {
        this.plugin.settings.offset_y = value;
        await this.plugin.saveSettings();
      })
    );
    new import_obsidian2.Setting(containerEl).setName("Use converting to jpg").addToggle((toggle) => {
      toggle.setValue(this.plugin.settings.use_jpg).onChange((value) => {
        this.plugin.settings.use_jpg = value;
        this.plugin.saveSettings();
      });
    });
    new import_obsidian2.Setting(containerEl).setName("Use converting to webp").addToggle((toggle) => {
      toggle.setValue(this.plugin.settings.use_webp).onChange((value) => {
        this.plugin.settings.use_webp = value;
        this.plugin.saveSettings();
      });
    });
    new import_obsidian2.Setting(containerEl).setName("Use converting to png").addToggle((toggle) => {
      toggle.setValue(this.plugin.settings.use_png).onChange((value) => {
        this.plugin.settings.use_png = value;
        this.plugin.saveSettings();
      });
    });
  }
};

// src/main.ts
var DEFAULT_SETTINGS = {
  quality: "0.8",
  offset_x: "0",
  offset_y: "0",
  use_jpg: true,
  use_webp: true,
  use_png: false
};
var ImageHelper = class extends import_obsidian3.Plugin {
  constructor() {
    super(...arguments);
    this.longTapTimeoutId = null;
  }
  async onload() {
    await this.loadSettings();
    if (import_obsidian3.Platform.isDesktop) {
      this.register(
        this.onElement(
          document,
          "contextmenu",
          "img",
          this.onClick.bind(this)
        )
      );
    }
    this.addSettingTab(new ICSettingTab(this.app, this));
  }
  onunload() {
  }
  onClick(event) {
    event.preventDefault();
    const target = event.target;
    const imgType = target.localName;
    const menu = new import_obsidian3.Menu();
    switch (imgType) {
      case "img": {
        const image = target.currentSrc;
        const originExtension = getExtension(image);
        const url = new URL(image);
        const protocol = url.protocol;
        let file = getFileByName(image);
        dbg("Clicked Image : ", file ? file.path : "NULL");
        switch (protocol) {
          case "app:":
          case "data:":
            if (this.settings.use_jpg && originExtension !== "jpg" && originExtension !== "jpeg") {
              menu.addItem(
                (item) => item.setIcon("image-file").setTitle("convert to jpeg image").setChecked(true).onClick(async () => {
                  if (file == null) {
                    return;
                  }
                  convertImage(
                    file,
                    image,
                    "image/jpeg",
                    "jpg",
                    Number(this.settings.quality)
                  );
                })
              );
            }
            if (this.settings.use_webp && originExtension !== "webp") {
              menu.addItem(
                (item) => item.setIcon("image-file").setTitle("convert to webp image").setChecked(true).onClick(async () => {
                  if (file == null) {
                    return;
                  }
                  convertImage(
                    file,
                    image,
                    "image/webp",
                    "webp",
                    Number(this.settings.quality)
                  );
                })
              );
            }
            if (this.settings.use_png && originExtension !== "png") {
              menu.addItem(
                (item) => item.setIcon("image-file").setTitle("convert to png image").setChecked(true).onClick(async () => {
                  if (file == null) {
                    return;
                  }
                  convertImage(
                    file,
                    image,
                    "image/png",
                    "png",
                    Number(this.settings.quality)
                  );
                })
              );
            }
            break;
          default:
            return;
        }
        break;
      }
      default:
        return;
    }
    menu.showAtPosition({
      x: event.pageX + parseInt(this.settings.offset_x),
      y: event.pageY + parseInt(this.settings.offset_y)
    });
    this.app.workspace.trigger("image-contextmenu:contextmenu", menu);
  }
  async loadSettings() {
    this.settings = Object.assign(
      {},
      DEFAULT_SETTINGS,
      await this.loadData()
    );
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
  onElement(el, event, selector, listener, options) {
    el.on(event, selector, listener, options);
    return () => el.off(event, selector, listener, options);
  }
};