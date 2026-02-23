import tseslint from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import eslintPluginPrettierRecommended from "eslint-plugin-prettier/recommended";

export default [
  {
    files: ["**/*.{ts,tsx,js,jsx}"],
    plugins: {
      "@typescript-eslint": tseslint,
    },
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: "module",
        ecmaFeatures: { jsx: true },
        project: "./tsconfig.json",
      },
    },
    rules: {
      eqeqeq: "error",
      "no-console": ["error", { allow: ["warn", "error"] }],
      "dot-notation": "error",
      "no-unused-vars": "off",
      "@typescript-eslint/no-unused-vars": [
        "error",
        { args: "after-used", vars: "all", ignoreRestSiblings: true },
      ],
      "import/order": "off",
      "simple-import-sort/imports": "off",
      "sort-imports": "off",
    },
    settings: {
      react: {
        version: "detect",
      },
      "import/resolver": {
        node: {
          extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
        },
        alias: {
          map: [["@", "./src"]],
          extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
        },
      },
    },
  },
  eslintPluginPrettierRecommended,
];
