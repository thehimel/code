# TypesScript

## Issue: WebStorm - Can not Import SVG Files in React Project

* Error message: `WebStorm: TS2307: Cannot find module ./assets/react.svg or its corresponding type declarations.`.

### Solution

* Create a `custom.d.ts` file: Create a file named custom.d.ts in the root of your project if it doesn't exist already.
  Inside `custom.d.ts`, add the following declaration to help TypeScript recognize SVG modules.

  ```typescript
  /*Any import ending with .svg should be treated as a module with the specified content.*/
  declare module "*.svg" {
    const content: string;
    export default content;
  }
  ```

* Add the `custom.d.ts` file to the `include` section if it's not already included.

```json
{
  "include": [
    "src",
    "custom.d.ts"
  ]
}
```

## Install Tailwindcss

* [How to Set up React and Tailwind CSS with Vite in a Project](https://www.freecodecamp.org/news/how-to-install-tailwindcss-in-react/)