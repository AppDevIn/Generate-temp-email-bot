module.exports = {
    types: [
        { types: ["feat", "feature"], label: "🎉 New Features" },
        { types: ["fix", "bugfix"], label: "🐛 Bugfixes" },
        { types: ["improvements", "enhancement"], label: "🔨 Improvements" },
        { types: ["perf"], label: "🏎️ Performance Improvements" },
        { types: ["build", "ci"], label: "🏗️ Build System" },
        { types: ["refactor"], label: "🪚 Refactors" },
        { types: ["doc", "docs"], label: "📚 Documentation Changes" },
        { types: ["test", "tests"], label: "🔍 Tests" },
        { types: ["chore"], label: "🧹 Chores" },
        { types: ["BREAKING"], label: "Breaking Changes" },
        { types: ["CI","ci"], label: "Making Changes to CI" },
        { types: ["CD","cd"], label: "Making Changes to CD" },
        { types: ["Merge branch"], label: "Branches Merged" },
        { types: ["Merge pull request"], label: "Pull Requests Merged" },
        { types: ["other"], label: "Other Changes" },
    ],

    excludeTypes: ["other"],

    renderTypeSection: function (label, commits) {
        let text = `\n## ${label}\n`;

        commits.forEach((commit) => {
            text += `- ${commit.subject} ([${commit.sha.substr(0, 6)}](${commit.url}))\n`;
        });

        return text;
    },

    renderChangelog: function (release, changes) {
        const now = new Date();
        return `# ${release} - ${now.toISOString().substr(0, 10)}\n` + changes + "\n\n";
    },
};
