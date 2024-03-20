import { defineConfig } from "vite";

// vite test config files

export default defineConfig({
    test: {
        includeSource: ["src/**/*,{js,ts}"],
        coverage: {
            reporter: ["text", "html"]
        }
    }
})