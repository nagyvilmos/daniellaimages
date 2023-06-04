<script>
  const config = {
    color: "#282230",       
    background: "#f1f1f1",  
    primary: "#005080",
    "primary-text": "#a5e0cf",
    secondary: "#499CBA",
    positive: "green",      
    "positive-text": "#f1f1f1",
    negative: "red",        
    error: "#FE2E64",       
    warning: "#FFBF00",     
    info: "#81F7D8",
  };

  const textColor = config.color // won't work without this.
  Object.keys(config).forEach((prop) => {
    const varString = `--theme-${prop}`;
    document.documentElement.style.setProperty(varString, config[prop]);
    if (!['color','background'].includes(prop) && !config[`${prop}-text`])
    {
      document.documentElement.style.setProperty(`${varString}-text`, textColor);
    }
  });

</script>

<slot>
  <!-- content will go here -->
</slot>

<style>
  :global(html) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-color);
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  }
  :global(.base) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-color);
  }
  :global(.reverse) {
    background-color: var(--theme-color);
    color: var(--theme-background);
    border-color: var(--theme-background);
  }
  :global(.primary) {
    background-color: var(--theme-primary);
    color: var(--theme-primary-text);
    border-color: var(--theme-primary-text);
  }
  :global(.primary-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-primary);
  }
  :global(.secondary) {
    background-color: var(--theme-secondary);
    color: var(--theme-secondary-text);
    border-color: var(--theme-secondary-text);
  }
  :global(.secondary-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-secondary);
  }
  :global(.positive) {
    background-color: var(--theme-positive);
    color: var(--theme-positive-text);
    border-color: var(--theme-positive-text);
  }
  :global(.positive-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-positive);
  }
  :global(.negative) {
    background-color: var(--theme-negative);
    color: var(--theme-negative-text);
    border-color: var(--theme-negative-text);
  }
  :global(.negative-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-negative);
  }
  :global(.error) {
    background-color: var(--theme-error);
    color: var(--theme-error-text);
    border-color: var(--theme-error-text);
  }
  :global(.error-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-error);
  }
  :global(.warning) {
    background-color: var(--theme-warning);
    color: var(--theme-warning-text);
    border-color: var(--theme-warning-text);
  }
  :global(.warning-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-warning);
  }
  :global(.info) {
    background-color: var(--theme-info);
    color: var(--theme-info-text);
    border-color: var(--theme-info-text);
  }
  :global(.info-reverse) {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-info);
  }
</style>
