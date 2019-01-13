export interface PreviewBlogContent {
  id: string;
  name: string;
  summary: string;
  createAt: number;
}
export interface PaginationPara {
  countAll: number,
  selectNow: number,
}
export interface BlogDetail {
  id: string;
  name: string;
  content: string;
  creatAt: number;
}