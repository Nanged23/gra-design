<style scoped>
.markdown-editor {
    height: 100vh;
    overflow-y: auto;
    margin-left: 240px;
    display: flex;
    /* 添加 flex 布局 */
    flex-direction: column;
    /* 主轴方向为垂直 */
}

.button-container {
    display: flex;
    justify-content: space-between;
    padding: 10px 5px;
}

.btn {
    display: grid;
    width: 45px;
    height: 40px;
    padding-left: 5px;
    align-items: center;
    justify-content: center;
    justify-items: center;
    background: #e3edf7;
    border-radius: 10px;
    box-shadow: 6px 6px 10px -1px rgba(0, 0, 0, 0.15),
        -6px -6px 10px -1px rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(0, 0, 0, 0);
    cursor: pointer;
    transition: transform 0.5s;
}

.btn:hover {
    box-shadow: inset 4px 4px 6px -1px rgba(0, 0, 0, 0.2),
        inset -4px -4px 6px -1px rgba(255, 255, 255, 0.7),
        -0.5px -0.5px 0px rgba(255, 255, 255, 1),
        0.5px 0.5px 0px rgba(0, 0, 0, 0.15),
        0px 12px 10px -10px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(0, 0, 0, 0.1);
    transform: translateY(0.5em);
}

.btn svg {
    transition: transform 0.5s;
    width: 25px;
    height: 25px;
}

.btn:hover svg {
    transform: scale(0.9);
    fill: #333333;
}

button {
    margin-top: 5px;
    padding: 0.1em 0.2em;
    width: 6em;
    height: 3.6em;
    background-color: #212121;
    border: 0.08em solid #fff;
    border-radius: 0.3em;
    font-size: 12px;
    cursor: pointer;
}

button span {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    bottom: 0.4em;
    width: 3.5em;
    height: 2.1em;
    background-color: #212121;
    border-radius: 0.2em;
    font-size: 1.5em;
    color: #fff;
    border: 0.08em solid #fff;
    box-shadow: 0 0.4em 0.1em 0.019em #fff;
}

button span:hover {
    transition: all 0.5s;
    transform: translate(0, 0.4em);
    box-shadow: 0 0 0 0 #fff;
}

button span:not(:hover) {
    transition: all 1s;
}

.editor-container {
    display: grid;
    grid-template-areas:
        "editor-title preview-title"
        "editor-content preview-content";
    grid-template-rows: auto 1fr;
    grid-template-columns: 1fr 1fr;
    min-height: 100%;
}

.editor-title {
    grid-area: editor-title;
    padding: 16px;
    border-bottom: 1px solid #e0e0e0;
    border-right: 1px solid #bed5c7;
    outline: none;
    text-align: center;
    /* 水平居中 */
    display: flex;
    /* 使用 flex 实现垂直居中 */
    align-items: center;
    /* 垂直居中 */
    justify-content: center;
    /* 水平居中 */
    height: 60px;
    /* 固定高度以确保居中效果明显 */
}

.editor-content {
    grid-area: editor-content;
    padding: 16px;
    white-space: pre-wrap;
    outline: none;
    line-height: 1.6;
    border-right: 1px solid #bed5c7;
    overflow-y: auto;
    height: auto;
    min-height: 600px;
}

.preview-title {
    grid-area: preview-title;
    padding: 16px;
    border-bottom: 1px solid #e0e0e0;
    text-align: center;
    /* 水平居中 */
    display: flex;
    /* 使用 flex 实现垂直居中 */
    align-items: center;
    /* 垂直居中 */
    justify-content: center;
    /* 水平居中 */
    height: 60px;
    /* 与编辑区标题高度一致 */
}

.preview-content {
    grid-area: preview-content;
    padding: 16px;
    line-height: 1.6;
    height: auto;
}

.editor-title:empty:before,
.editor-content:empty:before {
    content: attr(placeholder);
    color: #999;
    pointer-events: none;
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(237, 238, 237, 0.2);
    backdrop-filter: blur(4px);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    width: 16rem;
    min-height: 22rem;
    height: auto;
    /*控制弹窗*/
    background: linear-gradient(to top, rgba(215, 236, 251, 0.8), rgba(221, 210, 248, 0.4));

    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0.75rem;
    /* p-3 */
}

.form {
    color: #6366f1;
}

.fieldset {
    border: 4px dashed #a855f7;
    padding: 1.25rem;
    border-radius: 0.375rem;
}

.legend {
    text-align: center;
    padding-left: 0.5rem;
    /* px-2 */
    padding-right: 0.5rem;
    font-style: italic;
    margin-left: -0.5rem;
    /* -mx-2 */
}

.form-item {
    margin-bottom: 0.5rem;
    /* mb-2 */
}

.label {
    font-size: 0.75rem;
    /* text-xs */
    font-weight: bold;
}

.label::after {
    content: '*';
    color: #f87171;
    /* after:text-red-400 */
}

.input {
    width: 100%;
    padding: 0.5rem;
    /* p-2 */
    margin-bottom: 0.5rem;
    /* mb-2 */
    margin-top: 0.25rem;
    /* mt-1 */
    outline: none;
    border: none;
}

.input:focus {
    box-shadow: 2px solid #6366f1;
}

.image-preview {
    margin-top: 0.25rem;
    /* mt-1 */
    width: 100%;
    max-height: 100px;
    overflow: hidden;
    border-radius: 6px;
}

.image-preview img {
    width: 100%;
    height: auto;
    max-height: 100px;
    object-fit: contain;
}

.tags-container {
    margin-bottom: 0.25rem;
    /* mb-1 */
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
    /* gap-4 */
    align-items: center;
    font-size: 15px;
}

.tag {
    background: #e0e7ff;
    padding: 0.125rem 0.375rem;
    /* p-2 6px */
    border-radius: 12px;
    margin-right: 0.25rem;
    /* mr-4 */
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    /* gap-4 */
}

.tag span {
    cursor: pointer;
    color: #6366f1;
}

.form-actions {
    align-items: center;
    justify-items: center;
    display: flex;
    flex-direction: row;
    gap: 3.125rem;
    /* gap-50px */
    margin-top: 0.75rem;
    /* mt-3 */
}

.submit-btn {
    height: 100%;
    width: 100%;
    border-radius: 0.375rem;
    /* rounded-md */
    background-color: #c7d2fe;
    /* bg-indigo-200 */
    color: #4338ca;
    /* text-indigo-700 */
    padding: 0.5rem;
    /* p-2 */
    text-align: center;
    font-weight: bold;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    margin-top: 0.5rem;
    /* mt-2 */
    border: 1px solid #a5b4fc;
    /* border-indigo-300 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.submit-btn:hover {
    background-color: #4f46e5;
    /* hover:bg-indigo-400 */
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.close-btn {
    height: 100%;
    width: 100%;
    border-radius: 0.375rem;
    /* rounded-md */
    background-color: #c7d2fe;
    /* bg-indigo-200 */
    color: #4338ca;
    /* text-indigo-700 */
    padding: 0.5rem;
    /* p-2 */
    text-align: center;
    font-weight: bold;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    margin-top: 0.5rem;
    /* mt-2 */
    border: 1px solid #a5b4fc;
    /* border-indigo-300 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.close-btn:hover {
    background-color: #a5b4fc;
    /* hover:bg-indigo-300 */
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.modal-enter-active,
.modal-leave-active {
    transition: all 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
    opacity: 0;
    transform: scale(0.9);
}

.modal-enter-to,
.modal-leave-from {
    opacity: 1;
    transform: scale(1);
}
</style>
<template>
    <div class="markdown-editor">
        <div class="button-container">
            <div class="btn" role="button" tabindex="0" @click="goTo('/article')">
                <svg t="1742451580591" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="10936" width="70" height="70">
                    <path
                        d="M512 1024C229.248 1024 0 794.752 0 512S229.248 0 512 0s512 229.248 512 512-229.248 512-512 512z m0-938.666667C276.352 85.333333 85.333333 276.352 85.333333 512s191.018667 426.666667 426.666667 426.666667 426.666667-191.018667 426.666667-426.666667S747.648 85.333333 512 85.333333z m198.698667 625.365334a42.666667 42.666667 0 0 1-60.330667 0L512 572.330667l-138.368 138.368a42.666667 42.666667 0 0 1-60.330667-60.330667L451.669333 512 313.301333 373.632a42.666667 42.666667 0 0 1 60.330667-60.330667L512 451.669333l138.368-138.368a42.624 42.624 0 1 1 60.330667 60.330667L572.330667 512l138.368 138.368a42.666667 42.666667 0 0 1 0 60.330667z"
                        fill="#0092E4" p-id="10937"></path>
                </svg>
            </div>
            <button @click="showModal = true">
                <span>保存</span>
            </button>

            <!-- 弹窗 -->
            <transition name="modal">
                <div class="modal" v-if="showModal">
                    <div id="login" class="modal-content">
                        <form class="form" @submit.prevent="submitForm">
                            <fieldset class="fieldset">
                                <legend class="legend">挑选封面和标签</legend>

                                <!-- 图片上传 -->
                                <div class="form-item">
                                    <label class="label" for="image">👉 上传图片 </label>
                                    <input class="input" type="file" accept="image/*" @change="handleImageUpload"
                                        ref="fileInput">
                                    <div v-if="imagePreview" class="image-preview">
                                        <img :src="imagePreview" alt="预览">
                                    </div>
                                </div>

                                <!-- 标签输入 -->
                                <div class="form-item">

                                    <hr>

                                    <br>
                                    <label class="label" for="tags">👉 添加标签 </label>
                                    <div class="tags-container">
                                        <span>✓ 已添加标签：</span>
                                        <span v-for="(tag, index) in tags" :key="index" class="tag">
                                            {{ tag }}
                                            <span @click="removeTag(index)">×</span>
                                        </span>
                                    </div>
                                    <input v-model="currentTag" @keydown.enter.prevent="addTag" placeholder="按回车添加下一个"
                                        class="input">
                                </div>

                                <div class="form-actions">
                                    <button type="submit" class="submit-btn">提交</button>
                                    <button type="button" @click="showModal = false" class="close-btn">关闭</button>
                                </div>
                            </fieldset>
                        </form>
                    </div>
                </div>
            </transition>
        </div>
        <div class="editor-container">
            <div class="editor-title" ref="editorTitleRef" contenteditable="true" @input="handleTitleInput"
                @keydown="handleKeyDown" placeholder="输入标题..."></div>
            <div class="editor-content" ref="editorContentRef" contenteditable="true" @input="handleContentInput"
                @keydown="handleKeyDown" @click="handleClick" placeholder="记录内容..."></div>
            <div class="preview-title" ref="previewTitleRef" v-html="renderedTitle"></div>
            <div class="preview-content" ref="previewContentRef" v-html="renderedContent"></div>
        </div>
    </div>
</template>
<script setup>
import confetti from 'canvas-confetti'
import { ref, onMounted, computed, nextTick } from 'vue';
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';
import { useRouter } from 'vue-router';
import { writeArticle } from '../../js/cur/article.js';
import { ElMessage } from 'element-plus';
const router = useRouter();
const celebrate = () => {
  const count = 200;
  const defaults = {
    origin: { y: 0.7 }
  };

  function fire(particleRatio, opts) {
    confetti({
      ...defaults,
      ...opts,
      particleCount: Math.floor(count * particleRatio)
    });
  }

  fire(0.25, {
    spread: 26,
    startVelocity: 55,
  });
  fire(0.2, {
    spread: 60,
  });
  fire(0.35, {
    spread: 100,
    decay: 0.91,
    scalar: 0.8
  });
  fire(0.1, {
    spread: 120,
    startVelocity: 25,
    decay: 0.92,
    scalar: 1.2
  });
  fire(0.1, {
    spread: 120,
    startVelocity: 45,
  });
};
const goTo = (path) => {
    router.push(path);
};
const showModal = ref(false);
let imagePreview = ref(null);
let imageFile = ref(null);
const tags = ref([]);
const currentTag = ref('');
const editorTitleRef = ref(null);
const editorContentRef = ref(null);
const previewTitleRef = ref(null);
const previewContentRef = ref(null);
const title = ref('');
const content = ref('');
const currentSelection = ref({ start: 0, end: 0 });
const renderedTitle = computed(() => {
    return marked(title.value);
});
const renderedContent = computed(() => {
    return marked(content.value);
});

const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
        imageFile.value = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.value = e.target.result;
        };
        reader.readAsDataURL(file);
    }
};
const addTag = () => {
    if (currentTag.value.trim()) {
        tags.value.push(currentTag.value.trim());
        currentTag.value = '';
    }
};

const removeTag = (index) => {
    tags.value = tags.value.filter((_, i) => i !== index);
};
const submitForm = () => {
    const formData = {
        title: title.value,
        content: content.value,
        cover: imageFile.value ? imageFile.value : '',
        tags: tags.value.join(','),
        word_diff: content.value.length
    };
    saveArticle(formData);
    imagePreview.value = null;
    imageFile.value = null;
    tags.value = [];
    currentTag.value = '';
    showModal.value = false;
};
const saveArticle = async (data) => {
    try {
        const updatedData = { ...data, user_id: 123 };
        console.log(updatedData.tags.value);
        await writeArticle(updatedData);
        ElMessage({
            message: "新完成了一篇文章～",
            type: 'success',
        });
        celebrate();
        router.push('/article');
        
    } catch (error) {
        ElMessage({
            message: "文章保存出错了~稍后试试吧",
            type: 'error',
        });
        console.log(error);
    }
};
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

const handleTitleInput = (e) => {
    title.value = e.target.innerText;
    saveSelection(e.target);
};

const handleContentInput = async (e) => {
    await nextTick();
    content.value = e.target.innerText;
    saveSelection(e.target);
};
const handlePaste = async (e) => {
    e.preventDefault();
    try {
        const text = await navigator.clipboard.readText();
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);
        range.deleteContents();
        range.insertNode(document.createTextNode(text));
        content.value = editorContentRef.value.innerText;
        saveSelection(editorContentRef.value);
    } catch (err) {
        console.error('粘贴失败:', err);
    }
};

const saveSelection = (target) => {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const preCaretRange = range.cloneRange();
        preCaretRange.selectNodeContents(target);
        preCaretRange.setEnd(range.endContainer, range.endOffset);
        currentSelection.value = {
            start: preCaretRange.toString().length,
            end: preCaretRange.toString().length
        };
    }
};
const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
        e.preventDefault();
        const target = e.target === editorTitleRef.value ? editorTitleRef.value : editorContentRef.value;
        target.focus();
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);
        const fragment = document.createTextNode("    ");
        range.deleteContents();
        range.insertNode(fragment);
        range.setStartAfter(fragment);
        range.collapse(true);
        selection.removeAllRanges();
        selection.addRange(range);
        if (target === editorTitleRef.value) {
            title.value = target.innerText;
        } else {
            content.value = target.innerText;
        }
    } else if (e.key === 'Enter' && e.target === editorTitleRef.value) {
        e.preventDefault(); // 阻止标题区域换行
        editorContentRef.value.focus(); // 跳转到内容区域
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(editorContentRef.value);
        range.collapse(true); // 将光标置于内容区域开头
        selection.removeAllRanges();
        selection.addRange(range);
    }
};

const handleClick = (e) => {
    saveSelection(e.target);
};

onMounted(() => {
    if (editorTitleRef.value) {
        editorTitleRef.value.innerText = title.value;
    }
    if (editorContentRef.value) {
        editorContentRef.value.innerText = content.value;
        editorContentRef.value.addEventListener('paste', handlePaste);
    }
});

</script>
