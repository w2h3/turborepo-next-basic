module.exports = {
  reactStrictMode: true,
  transpilePackages: ["ui"],
  env: {
    process.env.VERCEL_ENV: 'production',
  },
};
