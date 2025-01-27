const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: "./src/index.js",
  plugins: [
    new CopyWebpackPlugin({
      patterns: [
        {
          from: "node_modules/@docsearch/js/dist/umd/index.js",
          to: path.resolve(
            __dirname,
            "src/crate/theme/rtd/crate/static/js/algolia.js"
          ),
        },
        {
          from: "node_modules/@fortawesome/fontawesome-free/css/all.min.css",
          to: path.resolve(
            __dirname,
            "src/crate/theme/rtd/crate/static/css/fontawesome.css"
          ),
        },
        {
          from: "node_modules/@fortawesome/fontawesome-free/webfonts/",
          to: path.resolve(
            __dirname,
            "src/crate/theme/rtd/crate/static/webfonts/"
          ),
        },
      ],
    }),
  ],
  module: {
    rules: [
      {
        test: [/\.css$/i, /\.s[ac]ss$/i],
        use: [
          { loader: "style-loader" },
          { loader: "css-loader", options: { sourceMap: true } },
          { loader: "postcss-loader", options: { sourceMap: true } },
          {
            loader: "sass-loader",
            options: { api: "legacy", sourceMap: true },
          },
        ],
      },
      {
        test: /\.(png|jpg|gif|svg|woff|woff2|eot|ttf|otf)$/i,
        type: "asset/resource",
      },
      {
        loader: "webpack-modernizr-loader",
        test: "/modernizr-config.json$/",
        type: "javascript/auto",
      },
      {
        // Expose jQuery for use outside Webpack build.
        test: require.resolve("jquery"),
        loader: "expose-loader",
        options: {
          exposes: ["$", "jquery", "jQuery"],
        },
      },
      {
        // Expose `js-cookie` for use outside Webpack build.
        test: require.resolve("js-cookie"),
        loader: "expose-loader",
        options: {
          exposes: ["Cookies"],
        },
      },
    ],
  },
  resolve: {
    alias: {
      modernizr$: path.resolve(__dirname, "modernizr-config.json"),
    },
  },
  output: {
    path: path.resolve(
      __dirname,
      "src",
      "crate",
      "theme",
      "rtd",
      "crate",
      "static",
      "bundle"
    ),
    filename: "main.js",
  },
};
