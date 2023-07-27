const path = require('path');

module.exports = {
    entry: './src/index.js',
    module: {
        rules: [
            {
                test: [
                    /\.css$/i,
                    /\.s[ac]ss$/i,
                ],
                use: [
                  { loader: "style-loader" },
                  { loader: "css-loader", options: { sourceMap: true } },
                  { loader: "postcss-loader", options: { sourceMap: true } },
                  { loader: "sass-loader", options: { sourceMap: true } },
                ],
            },
            {
                test: /\.(png|jpg|gif|svg|woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
            {
                loader: "webpack-modernizr-loader",
                test: "/modernizr-config\.json$/",
                type: 'javascript/auto',
            },
            {
                // Expose jQuery for use outside Webpack build.
                test: require.resolve('jquery'),
                loader: "expose-loader",
                options: {
                    exposes: ["$", "jquery", "jQuery"],
                },
            },
            {
                // Expose `js-cookie` for use outside Webpack build.
                test: require.resolve('js-cookie'),
                loader: "expose-loader",
                options: {
                    exposes: ["Cookies"],
                },
            },
        ],
    },
    resolve: {
        alias: {
            modernizr$: path.resolve(__dirname, 'modernizr-config.json'),
        },
    },
    output: {
        path: path.resolve(__dirname, 'src', 'crate', 'theme', 'rtd', 'crate', 'static', 'bundle'),
        filename: 'main.js',
    },
};
