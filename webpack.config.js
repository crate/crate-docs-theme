const path = require('path');

module.exports = {
    entry: './src/index.js',
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
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
