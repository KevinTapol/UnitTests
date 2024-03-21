import { defineConfig } from "vite";

// vite test config files

export default defineConfig({
    // this will make our if check to always false in our sum
    define: {
        "import.meta.vitest": "undefined",
    },
    test: {
        includeSource: ["src/**/*,{js,ts}"],
        coverage: {
            reporter: ["text", "html"]
        }
    }
})