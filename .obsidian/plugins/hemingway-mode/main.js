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

// main.ts
var main_exports = {};
__export(main_exports, {
  default: () => HemingwayModePlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var HEMINGWAY_MODE_CLASS = "hemingway";
var DEFAULT_SETTINGS = {
  enabled: false,
  allowBackspace: false,
  showToggleNotice: true,
  showStatusBar: true,
  statusBarText: "Hemingway"
};
var HemingwayModePlugin = class extends import_obsidian.Plugin {
  async onload() {
    this.addSettingTab(new HemingwayModeSettingTab(this.app, this));
    this.addCommand({
      id: "toggle-active",
      name: "Toggle active",
      callback: async () => {
        this.settings.enabled = !this.settings.enabled;
        await this.saveSettings();
        await this.updateStatus();
      }
    });
    this.addCommand({
      id: "set-active",
      name: "Set active",
      callback: async () => {
        this.settings.enabled = true;
        await this.saveSettings();
        await this.updateStatus();
      }
    });
    this.addCommand({
      id: "set-inactive",
      name: "Set inactive",
      callback: async () => {
        this.settings.enabled = false;
        await this.saveSettings();
        await this.updateStatus();
      }
    });
    this.registerEvent(
      this.app.workspace.on("active-leaf-change", async () => {
        await this.updateStatus(true);
      })
    );
    await this.loadSettings();
    this.buildKeyMapScope(this.settings.allowBackspace);
    this.keymapInstalled = false;
    await this.updateStatus(true);
    this.registerInterval(
      window.setInterval(async () => {
        const markdownView = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
        if (markdownView && this.settings.enabled) {
          if (markdownView.editor.hasFocus()) {
            await this.installHemingwayKeymap();
          } else {
            await this.uninstallHemingwayKeymap();
          }
        }
      }, 500)
    );
    const statusBarItem = this.addStatusBarItem();
    this.statusBar = statusBarItem.createSpan();
    this.statusBar.addClass("hemingway-mode-status");
  }
  async onunload() {
    if (this.settings.enabled) {
      await this.uninstallHemingwayKeymap();
      await this.restoreView();
    }
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
  onExternalSettingsChange() {
    this.updateStatus(true);
  }
  buildKeyMapScope(allowBackspace) {
    this.keyMapScope = new import_obsidian.Scope(this.app.scope);
    const nop = () => false;
    const voidKeys = [
      "ArrowLeft",
      "ArrowRight",
      "ArrowUp",
      "ArrowDown",
      "End",
      "Home",
      "PageUp",
      "PageDown",
      "Delete",
      "Clear",
      "Cut",
      "EraseEof",
      "Redo",
      "Undo"
    ];
    if (!allowBackspace) {
      voidKeys.push("Backspace");
    }
    for (const key of voidKeys) {
      this.keyMapScope.register([], key, nop);
      this.keyMapScope.register(["Meta"], key, nop);
      this.keyMapScope.register(["Alt"], key, nop);
      this.keyMapScope.register(["Ctrl"], key, nop);
      this.keyMapScope.register(["Shift"], key, nop);
      this.keyMapScope.register(["Mod"], key, nop);
      this.keyMapScope.register(["Meta", "Shift"], key, nop);
      this.keyMapScope.register(["Alt", "Shift"], key, nop);
      this.keyMapScope.register(["Ctrl", "Shift"], key, nop);
      this.keyMapScope.register(["Shift", "Shift"], key, nop);
      this.keyMapScope.register(["Mod", "Shift"], key, nop);
    }
    this.keyMapScope.register(["Meta"], "Z", nop);
    this.keyMapScope.register(["Meta"], "A", nop);
  }
  async updateStatus(quiet = false) {
    const markdownView = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
    if (!markdownView) {
      await this.uninstallHemingwayKeymap();
      await this.restoreView();
      return;
    }
    this.statusBar.setText(this.settings.showStatusBar && this.settings.enabled ? this.settings.statusBarText : "");
    if (this.settings.enabled) {
      await this.installHemingwayKeymap();
      await this.setupView();
    } else {
      await this.uninstallHemingwayKeymap();
      await this.restoreView();
    }
    if (this.settings.showToggleNotice && !quiet) {
      new import_obsidian.Notice(`Hemingway mode ${this.settings.enabled ? "active" : "inactive"}`, 2e3);
    }
  }
  async installHemingwayKeymap() {
    if (this.keymapInstalled)
      return;
    this.app.keymap.pushScope(this.keyMapScope);
    this.keymapInstalled = true;
  }
  async uninstallHemingwayKeymap() {
    if (!this.keymapInstalled)
      return;
    this.app.keymap.popScope(this.keyMapScope);
    this.keymapInstalled = false;
  }
  async setupView() {
    var _a;
    const markdownView = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
    if (markdownView && !markdownView.contentEl.classList.contains(HEMINGWAY_MODE_CLASS)) {
      (_a = markdownView.editor) == null ? void 0 : _a.setCursor({ line: 99999999, ch: 0 });
      markdownView.contentEl.addClass(HEMINGWAY_MODE_CLASS);
      markdownView.contentEl.addEventListener("click", this.mouseEventListener.bind(this));
    }
  }
  async restoreView() {
    const markdownView = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
    if (markdownView) {
      markdownView.contentEl.removeClass(HEMINGWAY_MODE_CLASS);
      markdownView.contentEl.removeEventListener("click", this.mouseEventListener.bind(this));
    }
  }
  mouseEventListener(ev) {
    var _a;
    ev.preventDefault();
    ev.stopPropagation();
    const markdownView = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
    (_a = markdownView == null ? void 0 : markdownView.editor) == null ? void 0 : _a.focus();
  }
};
var HemingwayModeSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian.Setting(containerEl).setName("Hemingway mode enabled").setDesc("Prevents any editing, so you can only write ahead.").addToggle(
      (toggle) => toggle.setValue(this.plugin.settings.enabled).onChange(async (value) => {
        this.plugin.settings.enabled = value;
        await this.plugin.saveSettings();
        await this.plugin.updateStatus(true);
      })
    );
    new import_obsidian.Setting(containerEl).setName("Show activation state in status bar").setDesc("Shows in the status bar when the write-only mode is active.").addToggle(
      (toggle) => toggle.setValue(this.plugin.settings.showStatusBar).onChange(async (value) => {
        this.plugin.settings.showStatusBar = value;
        await this.plugin.saveSettings();
        await this.plugin.updateStatus(true);
        this.display();
      })
    );
    if (this.plugin.settings.showStatusBar) {
      new import_obsidian.Setting(containerEl).setName("Text to show in status bar").setDesc("Appears in status bar when the write-only mode is active.").addText(
        (text) => text.setValue(this.plugin.settings.statusBarText).onChange(async (value) => {
          this.plugin.settings.statusBarText = value;
          await this.plugin.saveSettings();
          await this.plugin.updateStatus(true);
        })
      );
    }
    new import_obsidian.Setting(containerEl).setName("Show notice when toggling status").setDesc("Helps noticing changes between enabled and disabled.").addToggle(
      (toggle) => toggle.setValue(this.plugin.settings.showToggleNotice).onChange(async (value) => {
        this.plugin.settings.showToggleNotice = value;
        await this.plugin.saveSettings();
        await this.plugin.updateStatus(true);
      })
    );
    new import_obsidian.Setting(containerEl).setName("Allow using Backspace key even if active").setDesc("Allows deleting text with Backspace. This is useful for lousy typists.").addToggle(
      (toggle) => toggle.setValue(this.plugin.settings.allowBackspace).onChange(async (value) => {
        this.plugin.settings.allowBackspace = value;
        await this.plugin.saveSettings();
        this.plugin.buildKeyMapScope(this.plugin.settings.allowBackspace);
        await this.plugin.updateStatus(true);
      })
    );
  }
};
