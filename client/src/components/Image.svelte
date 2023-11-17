<script>
  export let image;
  export let large;
  console.log({ image, large });
</script>

<dialog open={large} >
  <h2>{image.description}</h2>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <img
    class={"large"}
    src={`resource/images/${image.name}`}
    alt={image.description}
    id={image.name}
    on:click
  />
  <p>
    {#each (image.tags || "untagged").split(" ").sort() as tag}
      <span class="badge">{tag}</span>
    {/each}
  </p>
</dialog>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<img
  class={"image"}
  src={`resource/images/${image.name}`}
  alt={image.description}
  id={image.name}
  on:click
/>

<style>
  dialog {
    top: 7vh;
    background-color: cornflowerblue;
    border: 4px solid darkblue;
    border-radius: 12px;
  }
  .large {
    max-width: 66vw;
    max-height: 66vh;
    margin: 8px;
    border: 4px solid darkblue;
    border-radius: 12px;
  }
  .image {
    max-width: 22vw;
    max-height: 22vh;
    margin: 4px;
    border: 2px solid grey;
    border-radius: 6px;
  }
  .badge {
    border-radius: 16px;
    border: 2px solid skyblue;
    background-color: cadetblue;
    color: aliceblue;
    padding: 2px 4px;
  }
</style>
