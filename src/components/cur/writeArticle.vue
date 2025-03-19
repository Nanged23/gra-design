<template>
    <div class="markdown-editor">
        <div class="editor-container">
            <div class="editor" ref="editorRef" contenteditable="true" @input="handleInput" @keydown="handleKeyDown"
                @click="handleClick"></div>

            <div class="preview" ref="previewRef" v-html="renderedHTML"></div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';
const previewRef = ref(null); 
marked.setOptions({
    highlight: function (code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            return hljs.highlight(code, { language: lang }).value;
        }
        return hljs.highlightAuto(code).value;
    },
    breaks: true,
    gfm: true
});

const editorRef = ref(null);
const content = ref('');
const currentSelection = ref({ start: 0, end: 0 });
const isEditing = ref(false);
const renderedHTML = computed(() => {
    return marked(content.value);
});

// Handle input events
const handleInput = (e) => {
    content.value = e.target.innerText;
    saveSelection();
    syncScroll(); // 添加滚动同步
};
const syncScroll = () => {
    if (!editorRef.value || !previewRef.value) return;

    const editor = editorRef.value;
    const preview = previewRef.value;

    // 计算编辑区的滚动比例
    const editorScrollRatio = editor.scrollTop / (editor.scrollHeight - editor.clientHeight);
    // 根据比例设置预览区的滚动位置
    const previewScrollTop = editorScrollRatio * (preview.scrollHeight - preview.clientHeight);

    preview.scrollTop = previewScrollTop;
};
// Save the current selection position
const saveSelection = () => {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const preCaretRange = range.cloneRange();
        preCaretRange.selectNodeContents(editorRef.value);
        preCaretRange.setEnd(range.endContainer, range.endOffset);
        currentSelection.value = {
            start: preCaretRange.toString().length,
            end: preCaretRange.toString().length
        };
    }
};

// Restore selection to a specific position
const restoreSelection = (start, end) => {
    const charIndex = start;
    const range = document.createRange();
    range.setStart(editorRef.value, 0);
    range.collapse(true);

    const nodeStack = [editorRef.value];
    let node, foundStart = false, stop = false;
    let charCount = 0;

    while (!stop && (node = nodeStack.pop())) {
        if (node.nodeType === 3) {
            const nextCharCount = charCount + node.length;
            if (!foundStart && charIndex >= charCount && charIndex <= nextCharCount) {
                range.setStart(node, charIndex - charCount);
                foundStart = true;
            }
            if (foundStart && end <= nextCharCount) {
                range.setEnd(node, end - charCount);
                stop = true;
            }
            charCount = nextCharCount;
        } else {
            let i = node.childNodes.length;
            while (i--) {
                nodeStack.push(node.childNodes[i]);
            }
        }
    }

    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
};
const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
        e.preventDefault();
        editorRef.value.focus();
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);
        const fragment = document.createTextNode("    ");
        range.deleteContents();
        range.insertNode(fragment); 
        range.setStartAfter(fragment);
        range.collapse(true);
        selection.removeAllRanges();
        selection.addRange(range); 
        content.value = editorRef.value.innerText;

    }
};
const handleClick = (e) => {
    isEditing.value = true;
    saveSelection();
};

// Initialize the editor with content
onMounted(() => {
    if (editorRef.value) {
        editorRef.value.innerText = content.value;
        editorRef.value.addEventListener('scroll', syncScroll);
    }
});
</script>

<style scoped>
.markdown-editor {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    margin-left: 230px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
   
}

.editor-container {
    display: flex;
    flex-direction: row;
    height: 700px;
}

.editor {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    white-space: pre-wrap;
    outline: none;
    line-height: 1.6;
    border-right: 1px solid #bed5c7;
}

.preview {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    border-top: 1px solid #e0e0e0;
    line-height: 1.6;
}

/* Markdown styling */
.preview h1 {
    font-size: 2em;
    margin-top: 0.67em;
    margin-bottom: 0.67em;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.3em;
}

.preview h2 {
    font-size: 1.5em;
    margin-top: 0.83em;
    margin-bottom: 0.83em;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.3em;
}

.preview h3 {
    font-size: 1.17em;
    margin-top: 1em;
    margin-bottom: 1em;
}

.preview p {
    margin-top: 1em;
    margin-bottom: 1em;
}

.preview ul,
.preview ol {
    padding-left: 2em;
    margin-top: 1em;
    margin-bottom: 1em;
}

.preview code {
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    background-color: rgba(27, 31, 35, 0.05);
    padding: 0.2em 0.4em;
    border-radius: 3px;
}

.preview pre {
    background-color: #f6f8fa;
    border-radius: 3px;
    padding: 16px;
    overflow: auto;
}

.preview pre code {
    background-color: transparent;
    padding: 0;
}

.preview blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
    margin: 1em 0;
}

.preview img {
    max-width: 100%;
}

.preview a {
    color: #0366d6;
    text-decoration: none;
}

.preview a:hover {
    text-decoration: underline;
}

.preview table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
}

.preview table th,
.preview table td {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
}

.preview table tr {
    background-color: #fff;
    border-top: 1px solid #c6cbd1;
}

.preview table tr:nth-child(2n) {
    background-color: #f6f8fa;
}
</style>