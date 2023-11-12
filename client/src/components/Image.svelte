<script>
    export let image;
    console.log(image)
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<img class="image"
    src={`resource/images/${image}`}
    alt={image}
    id={image}
    on:click={() => {}}
/>

<style>
    .image {
        max-width: 33vw;
        max-height: 33vh;
        margin: 4px;
        border: 2px solid;
        border-radius: 6px;
    }    
</style>