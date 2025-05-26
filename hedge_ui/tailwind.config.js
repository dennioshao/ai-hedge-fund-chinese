const path = require("path");

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
		colors:{
			background: "hsl(0, 0%, 100%)",
			foreground: "hsl(240, 10%, 10%)",
			border: "hsl(240, 5%, 90%)",
    		input: "hsl(240, 5%, 96%)",
    		ring: "hsl(240, 5%, 80%)"
		}
	}
  },
  plugins: []
}
