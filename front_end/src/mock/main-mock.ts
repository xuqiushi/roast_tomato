import Mock from 'mockjs'
export let start_mock = () => {
  Mock.mock(
    /api\/blog_list/,
    'post',
    {
      'previewBlogList|8': [
        {
          "id": "@string(20)",
          "name": '@title',
          "summary": '@cparagraph(5)',
          "createAt": '@integer(10)',
        }
      ]
    },
  )
  Mock.mock(
      /api\/get_blog_pagination/,
      'post',
      {
        'paginationPara': {
            "countAll|50-200": 100,
            "selectNow|1-50": 20,
          }
      },
  )
}
