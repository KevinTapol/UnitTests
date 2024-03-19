import { defineConfig } from "vite";

// vite test config files

export default defineConfig({
    test: {
        coverage: {
            reporter: ["text", "html"]
        }
    }
})