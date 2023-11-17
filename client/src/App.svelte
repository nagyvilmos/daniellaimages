<script>
  import { each } from "svelte/internal";
  //  import Carousel from "./components/Carousel.svelte";
  import ThemeContext from "./components/ThemeContext.svelte";
  import Page from "./pages/Page.svelte";
  import Image from "./components/Image.svelte";
  // const images = [
  //   {
  //     path: "https://picsum.photos/id/1012/3973/2639",
  //     id: "man-dog",
  //     alt: "A man with his faithless dog",
  //   },
  //   {
  //     path: "https://picsum.photos/id/237/200/300",
  //     id: "looking",
  //     alt: "Look at those puppy eyes",
  //   },
  //   {
  //     path: "https://picsum.photos/id/1020/4288/2848",
  //     id: "bear",
  //     alt: "A large smelly bear",
  //   },
  //   {
  //     path: "https://picsum.photos/id/1025/4951/3301",
  //     id: "dog",
  //     alt: "dog in a blanket",
  //   },
  //   {
  //     path: "https://picsum.photos/id/103/2592/1936",
  //     id: "field-feet",
  //     alt: "Feet in a field",
  //   },
  //   {
  //     path: "https://picsum.photos/id/104/3840/2160",
  //     id: "sky-hook",
  //     alt: "Some arty thing hanging from the sky",
  //   },
  // ];
  // ["800", "200", "300", "400", "500", "80", "2000"].forEach((square) =>
  //   images.push({
  //     path: `https://picsum.photos/${square}`,
  //     id: `square-${square}`,
  //     alt: `A square image ${square}px x ${square}px`,
  //   })
  // );

  async function fetchData() {
    const res = await fetch("/api/images");
    const data = await res.json();
    console.log({ data });
    if (res.ok) {
      return data;
    } else {
      throw new Error(data);
    }
  }

  let show = true;
  let selected = undefined;

  const setSelected = (image) => {
    selected = selected !== image ? image : undefined;
  };
</script>

<ThemeContext>
  <Page show={show}>
    {#await fetchData()}
      <p>loading</p>
    {:then images}
      <div style="height=64px" />
      {#each images as image}
        <Image
          {image}
          large={selected === image}
          on:click={() => setSelected(image)}
        />
      {/each}
    {:catch error}
      <p style="color: red">{error.message}</p>
    {/await}
  </Page>
</ThemeContext>
