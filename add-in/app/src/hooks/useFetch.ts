import { useQuery } from "@tanstack/react-query";

interface UseFetchProps<T, Args extends unknown[] = []> {
  key: string;
  fn: () => Promise<T>;
  enabled?: boolean;
  args?: Args;
  refetchInterval?: number;
}

export const useFetch = <T, Args extends unknown[] = []>({
  key,
  fn,
  args = [] as unknown as Args,
  enabled = true,
  refetchInterval,
}: UseFetchProps<T, Args>) => {
  const { data, isRefetching, isLoading, refetch } = useQuery<T>({
    queryKey: [key, ...args],
    queryFn: () => fn(),
    enabled: enabled,
    refetchInterval: refetchInterval ?? false,
  });
  return {
    data,
    isLoading,
    isRefetching,
    refetch,
  };
};
