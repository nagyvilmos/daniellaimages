<script>
    export let show
    console.log(show)
</script>

<div class="header">
    <h2>
        <span class="content">Daniella's Snaps</span>
        <span class="content">Contact me</span>
        <span class="content">About</span>
        <span class={show ? "show content" : "content"}>Random Show</span>
    </h2>
</div>

<style>
    .header {
        position: fixed;
        z-index: 2;
        top: 0;
        width: 100%;
        height: 64px;
        padding: 10px 16px;
        background: transparent;
    }

    .show {
        background-color: aqua;
    }
    .content {
        padding: 4px;
        border-width: 2px;
        border-style: solid;
        border-radius: 6px;
    }
</style>