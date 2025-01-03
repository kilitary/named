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
  default: () => SelectAndCompletePlugin
});
module.exports = __toCommonJS(main_exports);

// models/chat_llm.ts
var ChatInterface = class {
  constructor({ modelName, apiKey, maxTokens }) {
    this.apiKey = apiKey;
    this.modelName = modelName;
    this.maxTokens = maxTokens;
  }
  async generate(prompt) {
    return "";
  }
};
var ChatExecutor = class {
  constructor(model) {
    this.model = model;
  }
  async generate(prompt) {
    return this.model.generate(prompt);
  }
};

// models/model_claude.ts
var import_obsidian = require("obsidian");
var ClaudeModel = class extends ChatInterface {
  async generate(prompt) {
    const message = await (0, import_obsidian.requestUrl)({
      url: "https://api.anthropic.com/v1/messages",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": this.apiKey,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: this.modelName,
        max_tokens: +this.maxTokens,
        messages: [
          {
            role: "user",
            content: prompt
          }
        ]
      }),
      method: "POST"
    }).catch((error) => {
      console.error(error);
      return error;
    });
    return message.json.content[0].text;
  }
};

// models/model_openai.ts
var import_obsidian2 = require("obsidian");
var OpenAIModel = class extends ChatInterface {
  async generate(prompt) {
    const message = await (0, import_obsidian2.requestUrl)({
      url: "https://api.openai.com/v1/chat/completions",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${this.apiKey}`
      },
      body: JSON.stringify({
        model: this.modelName,
        max_tokens: +this.maxTokens,
        temperature: 0.5,
        messages: [
          {
            role: "user",
            content: prompt
          }
        ]
      }),
      method: "POST"
    }).catch((error) => {
      console.error(error);
      return error;
    });
    return message.json.content[0].text;
  }
};

// src/main.ts
var import_obsidian5 = require("obsidian");

// utils.ts
var getKeyNameBasedOnModel = (model) => {
  if (model.toLowerCase().startsWith("gpt"))
    return "openaiKey";
  if (model.toLowerCase().startsWith("claude"))
    return "antrhopicKey";
  return "openaiKey";
};

// src/components/FillerModal.ts
var import_obsidian3 = require("obsidian");
var FillerModal = class extends import_obsidian3.SuggestModal {
  constructor(fillers, prompt = "", callback) {
    super(app);
    this.prompt = prompt;
    this.fillers = fillers;
    this.callback = callback;
  }
  getSuggestions(query) {
    return this.fillers.filter((elem) => {
      return elem.name.toLowerCase().includes(query.toLowerCase()) || elem.content.toLowerCase().includes(query.toLowerCase());
    });
  }
  renderSuggestion(filler, el) {
    el.createEl("div", { text: filler.name });
    el.createEl("small", { text: filler.content.replace("{{PROMPT}}", this.prompt) });
  }
  onChooseSuggestion(item, evt) {
    this.callback(item);
  }
};

// src/utils/index.ts
function getSelectedText(editor) {
  const textSelection = getSelection();
  let selectedText = editor.getLine(editor.getCursor().line);
  if (textSelection !== null && textSelection.toString() !== "")
    selectedText = textSelection.toString();
  return { selectedText, textSelection };
}
var MODELS = {
  "GPT-3.5 Turbo": "gpt-3.5-turbo",
  "GPT-4": "gpt-4",
  "GPT-4 Turbo": "gpt-4-turbo",
  "Claude 3 Haiku": "claude-3-haiku-20240307",
  "Claude 3 Sonnet": "claude-3-sonnet-20240229",
  "Claude 3 Opus": "claude-3-opus-20240229"
};

// src/components/SettingsTab.ts
var import_obsidian4 = require("obsidian");
var MySettingTab = class extends import_obsidian4.PluginSettingTab {
  constructor(app2, plugin) {
    super(app2, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian4.Setting(containerEl).setName("Keys").setDesc("Add your API keys here").setHeading();
    new import_obsidian4.Setting(containerEl).setName("OpenAI API Key").setDesc("Input your OpenAI API key here.").addText((text) => text.setPlaceholder("Enter your secret").setValue(this.plugin.settings.openaiKey).onChange(async (value) => {
      this.plugin.settings.openaiKey = value;
      await this.plugin.saveSettings();
    }));
    new import_obsidian4.Setting(containerEl).setName("Anthropic API Key").setDesc("Input your Anthropic API key here.").addText((text) => text.setPlaceholder("Enter your secret").setValue(this.plugin.settings.antrhopicKey).onChange(async (value) => {
      this.plugin.settings.antrhopicKey = value;
      await this.plugin.saveSettings();
    }));
    new import_obsidian4.Setting(containerEl).setName("Model").setDesc("Choose the model you want to use").setHeading();
    new import_obsidian4.Setting(containerEl).setName("Choose your model").addDropdown((dropdown) => {
      Object.keys(MODELS).forEach((displayModelName) => {
        dropdown.addOption(MODELS[displayModelName], displayModelName);
      });
      dropdown.setValue(this.plugin.settings.model).onChange(async (value) => {
        this.plugin.settings.model = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian4.Setting(containerEl).setName("Max tokens").setDesc("The maximum number of tokens (words) to generate").addText((text) => text.setPlaceholder("600 (default)").setValue(this.plugin.settings.maxTokens).onChange(async (value) => {
      if (isNaN(+value)) {
        new import_obsidian4.Notice("Max tokens must be a number");
        return;
      }
      this.plugin.settings.maxTokens = value;
      await this.plugin.saveSettings();
    }));
    new import_obsidian4.Setting(containerEl).setName("Fillers").setDesc("Custom templates for all your needs").setHeading();
    const newFillerSetting = new import_obsidian4.Setting(containerEl).setName("Add Filler").setDesc("Add a new filler, use {{PROMPT}} to indicate where the prompt should be inserted").addTextArea((text) => {
    }).addButton((button) => button.setButtonText("Add").onClick(() => {
      const textArea = newFillerSetting.settingEl.querySelector("textarea");
      const fillerText = textArea == null ? void 0 : textArea.value;
      if (!fillerText) {
        new import_obsidian4.Notice("Filler text cannot be empty");
        return;
      }
      this.plugin.settings.fillers.push({
        name: `Filler ${this.plugin.settings.fillers.length + 1}`,
        content: fillerText
      });
      this.plugin.saveSettings();
      this.display();
    }));
    const listEl = containerEl.createEl("ul");
    listEl.style.listStyle = "none";
    listEl.style.padding = "0";
    listEl.style.margin = "0";
    this.plugin.settings.fillers.forEach((filler) => {
      const li = listEl.createEl("li");
      li.style.boxShadow = "0 0 5px rgba(0, 0, 0, 0.1)";
      li.style.padding = "10px";
      li.style.borderRadius = "0.5rem";
      li.style.display = "flex";
      li.style.justifyContent = "space-between";
      li.style.alignItems = "center";
      li.style.flexDirection = "row";
      li.style.marginBottom = "10px";
      const container = li.createDiv();
      container.createEl("div", { text: filler.name });
      container.createEl("small", { text: filler.content });
      const buttons = li.createDiv();
      buttons.style.display = "flex";
      buttons.style.gap = "0.5rem";
      buttons.createEl("button", { text: "Edit" }).addEventListener("click", () => {
        const modifyModal = new import_obsidian4.Modal(this.app);
        const { contentEl } = modifyModal;
        new import_obsidian4.Setting(contentEl).setName("Filler name").setClass("pt-2").addText((text) => text.setValue(filler.name).onChange(async (value) => {
          filler.name = value;
          this.display();
        }));
        new import_obsidian4.Setting(contentEl).setName("Filler content").addTextArea(
          (text) => text.setValue(filler.content).onChange(async (value) => {
            filler.content = value;
            this.display();
          })
        );
        modifyModal.open();
      });
      buttons.createEl("button", { text: "Delete" }).addEventListener("click", () => {
        const index = this.plugin.settings.fillers.findIndex((f) => f.name === filler.name);
        this.plugin.settings.fillers.splice(index, 1);
        this.plugin.saveSettings();
        this.display();
      });
    });
  }
};

// src/main.ts
var DEFAULT_SETTINGS = {
  openaiKey: "",
  antrhopicKey: "",
  model: "gpt-3.5-turbo",
  maxTokens: "600",
  fillers: []
};
var SelectAndCompletePlugin = class extends import_obsidian5.Plugin {
  async completeText(possiblePrefetchedText) {
    var _a;
    const editor = (_a = this.app.workspace.getActiveViewOfType(import_obsidian5.MarkdownView)) == null ? void 0 : _a.editor;
    if (!editor) {
      new import_obsidian5.Notice("No active editor found");
      return;
    }
    const {
      selectedText,
      textSelection
    } = getSelectedText(editor);
    try {
      new import_obsidian5.Notice("Generating text...");
      const message = await this.chatExecutor.generate(possiblePrefetchedText || selectedText);
      if (!textSelection) {
        editor.replaceRange("\n" + message, {
          line: editor.getCursor().line,
          ch: editor.getLine(editor.getCursor().line).length
        });
      } else {
        editor.replaceSelection(textSelection + "\n" + message);
      }
    } catch (error) {
      console.error(error);
      new import_obsidian5.Notice("Error generating text. Check the console for more information");
    }
  }
  setupLLM() {
    const keyName = getKeyNameBasedOnModel(this.settings.model);
    const apiKey = this.settings[keyName];
    const selectedModel = this.settings.model;
    const claudeModel = new ClaudeModel({
      modelName: selectedModel,
      apiKey,
      maxTokens: +this.settings.maxTokens
    });
    const openaiModel = new OpenAIModel({
      modelName: selectedModel,
      apiKey,
      maxTokens: +this.settings.maxTokens
    });
    switch (keyName) {
      case "openaiKey":
        this.chatExecutor = new ChatExecutor(openaiModel);
        break;
      case "antrhopicKey":
        this.chatExecutor = new ChatExecutor(claudeModel);
    }
  }
  openFillerModal() {
    var _a;
    const editor = (_a = this.app.workspace.getActiveViewOfType(import_obsidian5.MarkdownView)) == null ? void 0 : _a.editor;
    if (!editor) {
      new import_obsidian5.Notice("No active editor found");
      return;
    }
    const {
      selectedText
    } = getSelectedText(editor);
    new FillerModal(this.settings.fillers, selectedText, async (item) => {
      await this.completeText(item.content.replace("{{PROMPT}}", selectedText));
    }).open();
  }
  async onload() {
    await this.loadSettings();
    this.setupLLM();
    (0, import_obsidian5.addIcon)("complete_ai", `
			<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
				<path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 6.75 15.75v-1.5" />
			</svg>
		`);
    this.addRibbonIcon("complete_ai", "Select and Complete", async (evt) => {
      await this.completeText();
    });
    this.addCommand({
      id: "complete_text",
      name: "Complete selected text",
      callback: async () => {
        await this.completeText();
      }
    });
    this.addCommand({
      id: "complete_text_with_filler",
      name: "Complete selected text with custom prompt (fillers)",
      callback: async () => {
        this.openFillerModal();
      }
    });
    this.addSettingTab(new MySettingTab(this.app, this));
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};
